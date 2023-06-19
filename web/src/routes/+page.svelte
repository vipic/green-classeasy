<script lang="ts">
	import classNames from 'classnames';
	import { download, queryList, download_all } from '../services';

	let list = [];
	let selectValue = {};
	let inputValue;
	let downloadLoading = false;
	let showAlert = false;
	let alertInfo = {};
	let currentTimestmp;

	const getData = async () => {
		list = await queryList(inputValue, currentTimestmp);
		currentTimestmp = list[list.length - 1].timestamp;
	};

	const downloadImage = async () => {
		downloadLoading = true;
		alertInfo = await download(selectValue.id);
		showAlert = true;
		downloadLoading = false;
		setTimeout(() => {
			showAlert = false;
		}, 2000);
	};

	const downloadAllImage = async () => {
		alertInfo = await download_all();
		alert(alertInfo);
	};
</script>

<main>
	{#if showAlert}
		<div class="absolute top-1.5 right-1.5 w-1/4">
			<div class="alert shadow-lg">
				<div>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						class="stroke-info flex-shrink-0 w-6 h-6"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
						/></svg
					>
					<div>
						<h3 class="font-bold">{selectValue.title}</h3>
						<div class="text-xs">{alertInfo.count} 文件下载完成，耗时 {alertInfo.duration}秒</div>
					</div>
				</div>
				<div class="flex-none">
					<button
						class="btn btn-sm btn-primary"
						on:click={() => {
							showAlert = false;
						}}>确认</button
					>
				</div>
			</div>
		</div>
	{/if}
	<div class="p-4">
		<div class="mb-4">
			<input
				type="text"
				placeholder="请输入cookie"
				class="input input-sm input-bordered w-full max-w-xs"
				bind:value={inputValue}
			/>
			<button
				class={classNames({
					'btn btn-sm ml-4 mt-4': true,
					'btn-disabled': !inputValue
				})}
				on:click={getData}>获取</button
			>
			{#if currentTimestmp}
				<button
					class={classNames({
						'btn btn-sm ml-4 mt-4': true,
						'btn-disabled': !inputValue
					})}
					on:click={getData}>更早</button
				>
			{/if}
		</div>
		<div class="flex items-center">
			<label for="select1" class="mr-4">当日主题</label>
			<select
				id="select1"
				class="select select-sm select-bordered w-full max-w-xs"
				bind:value={selectValue}
			>
				<option disabled selected>选择查看的标题</option>
				{#each list as item}
					<option value={item}>{item.title}</option>
				{/each}
			</select>
			<button
				class={classNames({
					'btn btn-sm ml-4': true,
					'btn-disabled': downloadLoading
				})}
				on:click={downloadImage}
			>
				{#if downloadLoading}
					<span class="loading loading-spinner" />
				{/if}

				{downloadLoading ? '下载中...' : '下载'}</button
			>
			<button
				class={classNames({
					'btn btn-sm ml-4': true,
					'btn-disabled': downloadLoading
				})}
				on:click={downloadAllImage}
			>
				{#if downloadLoading}
					<span class="loading loading-spinner" />
				{/if}

				{downloadLoading ? '下载中...' : '批量下载'}</button
			>
		</div>
	</div>
</main>
