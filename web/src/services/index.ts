import request from '../utils/request';
import { ensureSite } from '../utils';
import { getContent, genImageList } from '../utils/data';

export const queryList = async (cookie: string, timestamp: number) => {
	try {
		const data = await request.post('/query', { cookie, timestamp });
		const ans = [];
		data.forEach((item) => {
			const { title, base_url, units, id, publish_time } = item;
			ans.push({
				title,
				baseUrl: ensureSite(base_url),
				units: genImageList(units),
				desc: getContent(units),
				timestamp: new Date(publish_time).getTime(),
				id
			});
		});
		return ans;
	} catch (e) {
		console.log(e);
		return [];
	}
};

export const download = async (id: string) => await request.post('/download', { id });

export const download_all = async (id: string) => await request.post('/download_all', { id });
