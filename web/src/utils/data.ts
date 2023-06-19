/**
 * 获取当日图片，类型为Upload的
 * @param input
 */
export const genImageList = (input) => {
	const ans = [];
	input.forEach((item) => {
		item.entries.forEach((inner) => {
			if (inner.t === 'Upload') {
				ans.push(...inner.value);
			}
		});
	});
	return ans;
};

/**
 * 获取当日评价，类型为TextArea且有值的
 * @param input
 * @returns {string}
 */
export const getContent = (input) => {
	let ans = '';
	input.forEach((item) => {
		item.entries.forEach((inner) => {
			if (inner.t === 'TextArea' && inner.value) {
				ans = inner.value;
				return;
			}
		});
	});
	return ans;
};
