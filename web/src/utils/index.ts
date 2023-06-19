export const ensureSite = (url: any): string => {
	try {
		new URL(url);
	} catch (error) {
		return `https://${url}`;
	}
	return url;
};
