export interface LabelBounds { left: number; top: number; right: number; bottom: number }

/** Keep complete labels readable, rather than painting one over another. */
export function reserveLabel(bounds: LabelBounds, occupied: LabelBounds[]): boolean {
  if (occupied.some(other => bounds.left < other.right && bounds.right > other.left && bounds.top < other.bottom && bounds.bottom > other.top)) return false;
  occupied.push(bounds);
  return true;
}
