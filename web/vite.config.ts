import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';
import postcss from './postcss.config.js';

export default defineConfig({
	plugins: [sveltekit()],
	css: {
		postcss
	},
	server: {
		port: 8087
	},
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});
