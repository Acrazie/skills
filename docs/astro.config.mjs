import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://skills.acrazie.dev',
  base: '/',
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
  ],
});
