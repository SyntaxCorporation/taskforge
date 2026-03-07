import { useState, useEffect } from "react";
import { changeStatus } from "../server_req.js";

function Task({ prop }) {
	const [status, setStatus] = useState(prop.status);
	let cStatus = async () => {
		try {
			const res = await changeStatus(prop.id, !status);
			setStatus(!status)
		} catch (err) {
			throw err;
		}
	};

	const buttons = [
		{
			name: "E",
			onClick: () => {}
		},
		{
			name: "D",
			onClick: () => {}
		}
	];
	return (
		<>
			<div className='w-full px-6 my-4'>
				<div className='bg-red-100 py-2 flex border border-gray-400 rounded-lg'>
					<div className='basis-[15%] flex items-center justify-center'>
						<div
							onClick={cStatus}
							className={`rounded-[50%] ${
								status ? "bg-blue-400" : "bg-transparent"
							} text-white h-[1.25rem] w-[1.25rem] border border-gray-400 text-sm flex items-center justify-center`}
						>
							{status ? "✓" : ""}
						</div>
					</div>
					<div className='basis-[65%] flex flex-col'>
            <div className='text-md leading-tight'>{prop.title}</div>
						<div className='text-[0.6rem] flex gap-1'>
							{prop.tags.map((element, index) => {
								return (
									<p
										className='mt-0.5 bg-amber-100 rounded py-[0.05rem] px-[0.5rem]'
										key={index}
									>
										{element}
									</p>
								);
							})}
						</div>
					</div>
					<div className='basis-[20%] flex items-center justify-center gap-4'>
						{buttons.map((element, index) => {
							return (
								<button key={index} onClick={element.onClick}>
									{element.name}
								</button>
							);
						})}
					</div>
				</div>
			</div>
		</>
	);
}

export default Task;
