import { useState, useEffect } from "react";
import Header from "./components/Header.jsx";
import Task from "./components/Task.jsx";
import Detail from "./components/Detail.jsx";
import { initData } from "./server_req.js";

function App() {
	const [data, setData] = useState([]);
	useEffect(() => {
		async function fetchData() {
			const res = await initData();
			if (!res.opr) {
				setData(res.data);
			} else {
				console.error(res.desc);
			}
		}
		fetchData();
	}, []);

	return (
		<>
			<Detail />
			<Header />
			{data.map((element, index) => {
				return <Task key={index} prop={element} />;
			})}
		</>
	);
}

export default App;
