/** @type {import('./$types').PageLoad} */
export const load = ({ url, route }) => {
	return {
		title: 'demo'
	};
};
export const prerender = false;
export const ssr = true;
