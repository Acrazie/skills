/** Bound motion even when the renderer is capable of running indefinitely. */
export function redrawDuration(signals: boolean, state: {
  visible: boolean; documentHidden: boolean; reduced: boolean; paused: boolean; hasConnections: boolean;
}): number {
  if (!state.visible || state.documentHidden) return 0;
  return signals && state.hasConnections && !state.reduced && !state.paused ? 1800 : 120;
}
