import {ensureSite} from '../src/utils/index';

describe('ensureSite function', () => {

	test('should return original URL for correctly formatted URLs', () => {
		expect(ensureSite('https://www.google.com')).toEqual('https://www.google.com');
		expect(ensureSite('http://www.google.com')).toEqual('http://www.google.com');
		expect(ensureSite('www.google.com')).toEqual('www.google.com');
	});

	test('should return modified URL for incorrectly formatted URLs', () => {
		expect(ensureSite('google.com')).toEqual('https://google.com');
		expect(ensureSite('ftp://google.com')).toEqual('https://ftp://google.com');
		expect(ensureSite('abc')).toEqual('https://abc');
	});

	test('should fail for non-string input', () => {
		expect(() => ensureSite(123)).toThrowError(TypeError);
		expect(() => ensureSite(null)).toThrowError(TypeError);
		expect(() => ensureSite(undefined)).toThrowError(TypeError);
	});

});
