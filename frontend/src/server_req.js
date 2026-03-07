import axios from "axios";

export async function addTask(data, spec_task) {
	try {
		if (spec_task) {
			const task = "add_task";
		} else {
			const task = "update_task";
		}
		const res = await axios.post("http://localhost:4444/", {
			data: data,
			task: "add",
			specific_task: task
		});
		return res.data;
	} catch (err) {
		throw err;
	}
}

export async function initData() {
	try {
		const res = await axios.post("http://localhost:4444/", {
			task: "init_data"
		});
		return res.data;
	} catch (err) {
		throw err;
	}
}

export async function search(query) {
	try {
		const res = await axios.post("http://localhost:4444/", {
			task: "search",
			query: query
		});
		return res.data;
	} catch (err) {
		throw err;
	}
}

export async function changeStatus(id, status) {
	try {
		const res = await axios.post("http://localhost:4444/", {
			task: "add",
			specific_task: "change_status",
			data: [status, id]
		});
		return res.data;
	} catch (err) {
		throw err;
	}
}
