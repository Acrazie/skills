/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        background: '#09090b',
        foreground: '#fafafa',
        muted: {
          DEFAULT: '#27272a',
          foreground: '#a1a1aa',
        },
        card: {
          DEFAULT: '#121215',
          foreground: '#fafafa',
          border: '#27272a',
        },
        accent: {
          DEFAULT: '#3f3f46',
          foreground: '#f4f4f5',
        },
        border: '#27272a',
        primary: {
          DEFAULT: '#fafafa',
          foreground: '#18181b',
        },
      },
      fontFamily: {
        sans: [
          'Inter',
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          'sans-serif',
        ],
        mono: [
          'JetBrains Mono',
          'ui-monospace',
          'SFMono-Regular',
          'Menlo',
          'Monaco',
          'Consolas',
          'monospace',
        ],
      },
    },
  },
  plugins: [],
};
