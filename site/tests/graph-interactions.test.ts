import { expect, test } from 'bun:test';
import fs from 'node:fs';
import { redrawDuration } from '../src/lib/graph-motion';

const source = fs.readFileSync(new URL('../src/scripts/skill-graph.ts', import.meta.url), 'utf8');

// Execute the shipped handlers with bounded renderer/timer doubles, not a fake DOM.
function dragHarness() {
  const motion = source.slice(source.indexOf('  function sleep()'), source.indexOf('  function select('));
  const listeners = source.split('\n').filter(line =>
    /(?:window|canvas)\.addEventListener\('(pointerdown|pointerup|pointercancel|lostpointercapture|blur|pagehide)'/.test(line)
  ).join('\n');
  return new Function('redrawDuration', `
    let dragging = false, resuming = false, stopTimer, timer;
    let pauses = 0, resumes = 0;
    const handlers = new Map();
    const target = name => ({ addEventListener: (event, handler) => handlers.set(name + ':' + event, handler) });
    const window = target('window'), canvas = target('canvas');
    const root = { dataset: {} }, visible = true, document = { hidden: false };
    const reduced = { matches: false }, manualPause = false, neighbors = new Set();
    const linked = () => false;
    const graph = {
      linkDirectionalParticles() { return this; },
      pauseAnimation() { pauses++; return this; },
      resumeAnimation() { resumes++; return this; }
    };
    const setTimeout = callback => { timer = callback; return 1; };
    const clearTimeout = () => { timer = undefined; };
    ${motion}
    ${listeners}
    return {
      dispatch: event => { const handler = handlers.get(event); if (!handler) throw new Error('Missing handler: ' + event); handler(); },
      flush: () => { const callback = timer; timer = undefined; callback?.(); },
      state: () => ({ dragging, pauses, resumes, animation: root.dataset.animation })
    };
  `)(redrawDuration);
}

for (const event of ['window:blur', 'window:pagehide', 'canvas:pointercancel']) {
  test(`${event} ends an interrupted drag and stops animation immediately`, () => {
    const harness = dragHarness();
    harness.dispatch('canvas:pointerdown');
    expect(harness.state().dragging).toBe(true);
    harness.dispatch(event);
    expect(harness.state()).toMatchObject({ dragging: false, animation: 'paused', pauses: 1 });
    harness.flush();
    harness.dispatch('canvas:pointerdown');
    harness.dispatch('window:pointerup');
    harness.flush();
    expect(harness.state()).toMatchObject({ dragging: false, animation: 'paused', pauses: 2 });
  });
}

test('lost pointer capture ends dragging and permits the redraw timeout to sleep', () => {
  const harness = dragHarness();
  harness.dispatch('canvas:pointerdown');
  harness.dispatch('canvas:lostpointercapture');
  expect(harness.state().dragging).toBe(false);
  harness.flush();
  expect(harness.state()).toMatchObject({ animation: 'paused', pauses: 1 });
});

const hashHandler = source.slice(source.indexOf('  const fromHash ='), source.indexOf('  fromHash();'));
for (const hash of ['', '#other-section', '#map-skill-unknown-acrazie', '#map-skill-']) {
  test(`hash ${JSON.stringify(hash)} clears stale selection`, () => {
    let selected: string | null = 'interview-acrazie';
    const data = { nodes: [{ id: 'interview-acrazie' }] };
    const select = (id: string | null) => {
      if (id && !data.nodes.some(node => node.id === id)) return;
      selected = id;
    };
    new Function('location', 'data', 'select', `${hashHandler}; fromHash();`)({ hash }, data, select);
    expect(selected).toBeNull();
  });
}

test('known skill hash retains deep-link selection', () => {
  let selected: string | null = null;
  const data = { nodes: [{ id: 'interview-acrazie' }] };
  new Function('location', 'data', 'select', `${hashHandler}; fromHash();`)(
    { hash: '#map-skill-interview-acrazie' }, data, (id: string | null) => { selected = id; }
  );
  expect(selected).toBe('interview-acrazie');
});
