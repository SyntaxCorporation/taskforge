import { useState } from "react";

function Header() {
	return (
		<>
			<div className='grid grid-cols-2 w-full px-6 py-3 shadow-md backdrop-blur-[4px] top-0 sticky'>
				<div className='text-2xl font-mono font-semibold'>TaskForge</div>
				<div className='flex items-center justify-end gap-4'>
					<button 
					onClick={() => {}}
					className='text-gray-400'>S</button>
					<button
						onClick={() => {}}
						className='bg-red-400 rounded text-white px-3'>
						Add Task
					</button>
				</div>
			</div>
		</>
	);
}

export default Header;
