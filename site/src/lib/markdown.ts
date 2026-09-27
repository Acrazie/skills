import { marked } from 'marked';

export function renderMarkdownWithHeadingOffset(content: string, offset: number): string {
  const tokens = marked.lexer(content);
  for (const token of tokens) {
    if (token.type === 'heading') token.depth = Math.min(6, token.depth + offset);
  }
  return marked.parser(tokens);
}
