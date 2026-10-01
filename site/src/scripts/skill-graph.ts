import type ForceGraph from 'force-graph';
import type { LinkObject, NodeObject } from 'force-graph';
import type { Invocation } from '../lib/skill-graph';
import { redrawDuration } from '../lib/graph-motion';
import { graphTranslations } from '../i18n/graph';
interface MapNode extends NodeObject { id: string; category: string; color: string; x: number; y: number }
interface MapLink extends LinkObject<MapNode> { source: string | MapNode; target: string | MapNode }
interface MapData { nodes: MapNode[]; links: Invocation[]; labels: typeof graphTranslations.en }
const root = document.querySelector<HTMLElement>('[data-skill-map]');
if (root) void setupMap(root);
async function setupMap(root: HTMLElement) {
  const data: MapData = JSON.parse(root.querySelector('[data-graph-data]')!.textContent!);
  const stage = root.querySelector<HTMLElement>('[data-stage]')!;
  const canvas = root.querySelector<HTMLElement>('[data-canvas]')!;
  const reader = root.querySelector<HTMLElement>('.map-reader')!;
  const contents = [...root.querySelectorAll<HTMLDetailsElement>('[data-content]')];
  const search = root.querySelector<HTMLInputElement>('[data-search]')!;
  const rows = [...root.querySelectorAll<HTMLElement>('[data-skill-row]')];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let graph: ForceGraph<MapNode, MapLink> | undefined;
  let selected: string | null = null;
  let hovered: string | null = null;
  let neighbors = new Set<string>();
  let matches = new Set(data.nodes.map(node => node.id));
  let manualPause = false;
  let visible = true;
  let dragging = false;
  let resuming = false;
  let stopTimer: ReturnType<typeof setTimeout> | undefined;
  const endpoint = (value: string | MapNode) => typeof value === 'string' ? value : value.id;
  const linked = (link: MapLink) => !!selected && (endpoint(link.source) === selected || endpoint(link.target) === selected);
  const controls = root.querySelector<HTMLElement>('[data-controls]')!;
  const pause = root.querySelector<HTMLButtonElement>('[data-pause]')!;
  const welcome = root.querySelector<HTMLElement>('[data-welcome]')!;
  const clear = root.querySelector<HTMLButtonElement>('[data-clear]')!;
  root.dataset.enhanced = 'true';
  contents.forEach(content => { content.hidden = true; });
  if (matchMedia('(max-width: 800px)').matches) root.querySelector<HTMLDetailsElement>('.map-directory')!.open = false;
  // Explicitly stop RAFs: force-graph's autoPauseRedraw alone still schedules a loop.
  function sleep() {
    if (stopTimer) clearTimeout(stopTimer);
    graph?.linkDirectionalParticles(0).pauseAnimation();
    root.dataset.animation = 'paused';
  }
  function wake(signals = false) {
    if (!graph || resuming) return;
    const duration = redrawDuration(signals, { visible, documentHidden: document.hidden, reduced: reduced.matches, paused: manualPause, hasConnections: neighbors.size > 1 });
    if (!duration) return sleep();
    if (stopTimer) clearTimeout(stopTimer);
    const animateSignals = duration > 120;
    // resumeAnimation synchronously draws and may emit onZoom before storing its RAF id.
    resuming = true;
    try { graph.linkDirectionalParticles(link => animateSignals && linked(link) ? 2 : 0).resumeAnimation(); }
    finally { resuming = false; }
    root.dataset.animation = animateSignals ? 'signals' : 'redraw';
    stopTimer = setTimeout(() => { if (!dragging) sleep(); }, duration);
  }
  function select(id: string | null, focus = false) {
    if (id && !data.nodes.some(node => node.id === id)) return;
    selected = id;
    neighbors = new Set(id ? [id] : []);
    for (const link of data.links) if (link.source === id || link.target === id) { neighbors.add(link.source); neighbors.add(link.target); }
    welcome.hidden = !!id; clear.hidden = !id;
    for (const content of contents) { content.hidden = content.dataset.content !== id; content.open = content.dataset.content === id; }
    root.querySelectorAll<HTMLAnchorElement>('[data-select]').forEach(anchor => {
      if (anchor.dataset.select === id) anchor.setAttribute('aria-current', 'true'); else anchor.removeAttribute('aria-current');
    });
    root.querySelector<HTMLElement>('[data-selection-status]')!.textContent = id ? `${data.labels.chosen}: ${id}` : '';
    reader.scrollTop = 0;
    if (focus && id) {
      const heading = root.querySelector<HTMLElement>(`[data-content="${id}"] h2`)!;
      heading.focus({ preventScroll: true });
      if (matchMedia('(max-width: 800px)').matches) heading.scrollIntoView({ behavior: reduced.matches ? 'instant' : 'smooth', block: 'start' });
    }
    graph?.linkColor(link => linked(link) ? '#e6d6ff' : '#767481').linkWidth(link => linked(link) ? 1.8 : 1);
    wake(true);
  }
  root.addEventListener('click', event => {
    const anchor = (event.target as Element).closest<HTMLAnchorElement>('[data-select]');
    if (!anchor || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault(); select(anchor.dataset.select!, true);
    history.replaceState(null, '', `#map-skill-${anchor.dataset.select}`);
  });
  clear.addEventListener('click', () => { select(null); history.replaceState(null, '', location.pathname + location.search); search.focus(); });
  search.addEventListener('input', () => {
    const query = search.value.trim().toLocaleLowerCase(); matches = new Set();
    if (query) root.querySelector<HTMLDetailsElement>('.map-directory')!.open = true;
    for (const row of rows) {
      row.hidden = !row.dataset.searchText!.includes(query);
      if (!row.hidden) matches.add(row.querySelector<HTMLElement>('[data-select]')!.dataset.select!);
    }
    root.querySelector<HTMLElement>('[data-empty]')!.hidden = matches.size > 0;
    const count = root.querySelector<HTMLElement>('[data-result-count]')!;
    count.textContent = `${matches.size} / ${data.nodes.length}`; count.setAttribute('role', 'status');
    graph?.nodeVisibility(node => matches.has(node.id)).linkVisibility(link => matches.has(endpoint(link.source)) && matches.has(endpoint(link.target)));
    wake();
  });
  function arrange() {
    if (!graph) return;
    const compact = stage.clientWidth < 500;
    graph.graphData().nodes.forEach((node, index) => {
      const original = data.nodes[index];
      node.x = node.fx = compact ? (index % 2 ? 90 : -90) : original.x;
      node.y = node.fy = compact ? (Math.floor(index / 2) - Math.floor(data.nodes.length / 4)) * 62 : original.y;
    });
  }
  function fit() { graph?.zoomToFit(0, stage.clientWidth < 500 ? 90 : 85); wake(); }
  root.querySelector('[data-reset]')!.addEventListener('click', fit);
  root.querySelector('[data-zoom-in]')!.addEventListener('click', () => { if (graph) graph.zoom(Math.min(4, graph.zoom() * 1.35), 0); wake(); });
  root.querySelector('[data-zoom-out]')!.addEventListener('click', () => { if (graph) graph.zoom(Math.max(.15, graph.zoom() / 1.35), 0); wake(); });
  pause.addEventListener('click', () => {
    manualPause = !manualPause; pause.textContent = manualPause ? data.labels.resume : data.labels.pause;
    pause.setAttribute('aria-pressed', String(manualPause)); wake(!manualPause);
  });
  reduced.addEventListener('change', () => { pause.hidden = reduced.matches; wake(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) sleep(); else wake(); });
  const observer = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; if (visible) wake(); else sleep(); });
  observer.observe(stage);
  const fromHash = () => { const prefix = '#map-skill-'; if (location.hash.startsWith(prefix)) select(location.hash.slice(prefix.length)); };
  fromHash(); window.addEventListener('hashchange', fromHash);
  let resize: ResizeObserver | undefined;
  window.addEventListener('pagehide', sleep);
  window.addEventListener('pageshow', () => wake());
  try {
    const { default: Graph } = await import('force-graph');
    if (!document.createElement('canvas').getContext('2d')) throw new Error('Canvas unavailable');
    graph = new Graph<MapNode, MapLink>(canvas)
      .width(stage.clientWidth).height(stage.clientHeight).backgroundColor('#101011')
      .graphData({ nodes: data.nodes.map(n => ({ ...n })), links: data.links.map(l => ({ source: l.source, target: l.target })) })
      .cooldownTicks(0).enableZoomInteraction(event => event.type !== 'wheel' || stage.clientWidth >= 500).minZoom(.15).maxZoom(4).nodeLabel(() => '').linkLabel(() => '')
      .linkColor('#767481').linkWidth(1).linkCurvature(.14)
      .linkDirectionalArrowLength(6).linkDirectionalArrowRelPos(.86)
      .linkDirectionalParticleWidth(2).linkDirectionalParticleColor('#e6d6ff').linkDirectionalParticleSpeed(.008)
      .onRenderFramePre((context, scale) => {
        const nodes = graph!.graphData().nodes;
        for (const category of new Set(nodes.map(n => n.category))) {
          const family = nodes.filter(n => n.category === category);
          const left = Math.min(...family.map(n => n.x)) - 34 / scale;
          const top = Math.min(...family.map(n => n.y)) - 46 / scale;
          const right = Math.max(...family.map(n => n.x)) + 34 / scale;
          const bottom = Math.max(...family.map(n => n.y)) + 52 / scale;
          context.strokeStyle = family[0].color; context.lineWidth = 1 / scale;
          context.globalAlpha = selected && !family.some(n => neighbors.has(n.id)) ? .07 : .24;
          const arm = 18 / scale;
          context.beginPath();
          context.moveTo(left + arm, top); context.lineTo(left, top); context.lineTo(left, top + arm);
          context.moveTo(right - arm, bottom); context.lineTo(right, bottom); context.lineTo(right, bottom - arm);
          context.stroke();
        }
        context.globalAlpha = 1;
      })
      .nodeCanvasObject((node, context, scale) => {
        const active = node.id === selected || node.id === hovered;
        const dim = !!selected && !neighbors.has(node.id) && !active;
        context.globalAlpha = dim ? .34 : 1;
        const size = (active ? 10 : 7) / scale;
        context.fillStyle = '#101011'; context.strokeStyle = node.color; context.lineWidth = (active ? 2 : 1.5) / scale;
        context.beginPath(); context.rect(node.x - size, node.y - size, size * 2, size * 2); context.fill(); context.stroke();
        context.fillStyle = node.color; context.fillRect(node.x - 1.5 / scale, node.y - 1.5 / scale, 3 / scale, 3 / scale);
        if (scale >= .25 || active) {
          context.font = `${11 / scale}px "JetBrains Mono", monospace`; context.textAlign = 'center';
          const words = node.id.replace(/-acrazie$/, '').split('-'); const lines: string[] = []; let line = '';
          for (const word of words) { if (line.length + word.length > 20 && line) { lines.push(line); line = word; } else line += (line ? '-' : '') + word; }
          lines.push(line);
          lines.forEach((text, index) => {
            const y = node.y + size + (16 + index * 14) / scale; const width = context.measureText(text).width;
            context.fillStyle = '#101011'; context.fillRect(node.x - width / 2 - 3 / scale, y - 11 / scale, width + 6 / scale, 14 / scale);
            context.fillStyle = active ? '#ffffff' : '#e0e0e5'; context.fillText(text, node.x, y);
          });
        }
        context.globalAlpha = 1;
      })
      .nodePointerAreaPaint((node, color, context, scale) => { context.fillStyle = color; const r = 22 / scale; context.fillRect(node.x - r, node.y - r, 2 * r, 2 * r); if (scale >= .25) context.fillRect(node.x - 72 / scale, node.y + 8 / scale, 144 / scale, 43 / scale); })
      .onNodeClick(node => { select(node.id, true); history.replaceState(null, '', `#map-skill-${node.id}`); })
      .onNodeHover(node => { hovered = node?.id ?? null; wake(); })
      .onNodeDragEnd(node => { node.fx = node.x; node.fy = node.y; wake(); })
      .onZoom(() => wake());
    canvas.querySelector('canvas')?.setAttribute('aria-hidden', 'true');
    canvas.addEventListener('pointermove', () => wake());
    canvas.addEventListener('pointerdown', () => { dragging = true; wake(); });
    window.addEventListener('pointerup', () => { dragging = false; wake(); });
    canvas.addEventListener('pointercancel', () => { dragging = false; sleep(); });
    canvas.addEventListener('wheel', () => wake(), { passive: true });
    resize = new ResizeObserver(() => { graph?.width(stage.clientWidth).height(stage.clientHeight); arrange(); fit(); }); resize.observe(stage);
    root.querySelector<HTMLElement>('[data-loading]')!.hidden = true;
    root.querySelector<HTMLElement>('[data-hint]')!.hidden = false;
    controls.hidden = false; pause.hidden = reduced.matches;
    arrange(); fit(); select(selected);
  } catch (error) {
    sleep(); graph?._destructor(); controls.hidden = true;
    root.querySelector<HTMLElement>('[data-loading]')!.textContent = data.labels.error;
    root.dataset.mapError = 'true'; console.error('Skill map could not initialize', error);
  }
}
