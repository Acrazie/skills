import { marked } from 'marked';

export function renderMarkdownWithHeadingOffset(content: string, offset: number, baseUrl?: string): string {
  const tokens = marked.lexer(content);
  for (const token of tokens) {
    if (token.type === 'heading') token.depth = Math.min(6, token.depth + offset);
  }
  if (baseUrl) marked.walkTokens(tokens, token => {
    if ((token.type === 'link' || token.type === 'image') && !/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(token.href)) {
      token.href = new URL(token.href, baseUrl).href;
    }
  });
  return marked.parser(tokens);
}
