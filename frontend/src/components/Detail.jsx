import { useState, useEffect, useRef } from "react";
import { addTask } from "../server_req.js";

function Detail() {
	const [saveStatus, setSaveStatus] = useState(false);
	const [addTagStatus, setAddTagStatus] = useState(false);
	const tagInput = useRef(null);
	const data = new Array();
	const tags = new Array();
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");
	tags.push("tag2");

	return (
		<>
			<div className='hidden fixed top-[50%] left-[50%] translate-[-50%] backdrop-blur-[6px] rounded-lg w-[70%] h-[60%] flex flex-col p-4 backdrop-brightness-[95%] border border-gray-400'>
				<div className='basis-[90%]'>
					<label>Title:</label>
					<input
						type='text'
						className='border border-gray-400 rounded outline-none px-3 py-0.5'
						placeholder='Enter Title'
						value=''
					/>
					<label>Tags:</label>
					<div className='flex'>
						<div
							className={`${
								addTagStatus ? "" : "hidden"
							} basis-[100%] flex gap-2`}
						>
							<input
								type='text'
								ref={tagInput}
								className='border border-gray-400 outline-none rounded px-3 py-0.5 w-full'
							/>
							<button
								className='border border-gray-400 px-3 py-0.5 rounded'
								onClick={() => {
									tags.push(tagInput.current.value);
									setAddTagStatus(false);
								}}
							>
								Add
							</button>
						</div>
						<div
							className={`${
								!addTagStatus ? "" : "hidden"
							} flex basis-[100%] relative`}
						>
							<div className='basis-[90%] overflow-x-scroll flex items-center text-[0.6rem] gap-1 w-[90%] absolute'>
								{tags.map((element, index) => {
									return (
										<div className='px-1 rounded bg-amber-100' key={index}>
											{element}
										</div>
									);
								})}
							</div>
							<button
								className='basis-[10%] w-[10%] absolute right-0 top-0'
								onClick={() => setAddTagStatus(true)}
							>
								+
							</button>
						</div>
					</div>
				</div>
				<div className='basis-[10%] grid grid-cols-2 font-mono'>
					<button onClick={() => {}}>Cencel</button>
					<button onClick={() => {}}>Save</button>
				</div>
			</div>
		</>
	);
}

export default Detail;
