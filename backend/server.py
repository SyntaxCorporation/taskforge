import sqlite3
import json
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

conn = sqlite3.connect("./database.db", check_same_thread=False)
cursor = conn.cursor()
ctime = int(datetime.now().timestamp())
cursor.execute("""
	CREATE TABLE IF NOT EXISTS tasks (
		id INTEGER PRIMARY KEY,
		title TEXT,
		tags TEXT,
		due DATE,
		note TEXT,
		status BOOLEAN,
		timestamp INTEGER
	)
""")

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

def ids_function(mode, cdata):

	if mode == "s2c":
		s_ids = []
		if not cdata:
			raw_sdata = cursor.execute("SELECT id FROM tasks").fetchall()
			return [row[0] for row in raw_sdata]
		raw_sdata = cursor.execute("SELECT id, timestamp FROM tasks").fetchall()
		sdata = {row[0]: row[1] for row in raw_sdata}
		for s_id in sdata.keys():
			if s_id not in cdata.keys():
				s_ids.append(s_id)
			elif sdata[s_id] > cdata[s_id]:
				s_ids.append(s_id)
		return s_ids

	elif mode == "c2s":
		c_ids = []
		raw_sdata = cursor.execute("SELECT id, timestamp FROM tasks").fetchall()
		if not raw_sdata:
			return cdata.keys()
		sdata = {row[0]: row[1] for row in raw_sdata}
		for c_id in cdata.keys():
			if c_id not in sdata.keys():
				c_ids.append(c_id)
			elif cdata[s_id] > sdata[s_id]:
				c_ids.append(c_id)
		return c_ids

	else:
		return {"opr":1, "desc": "Invalid Mode..."}
	

@app.post("/")
async def main(request: Request):
	req = await request.json()
	if req["task"] == "pull":
		server_ids = ids_function("s2c", req["data"])
		if server_ids:
			placeholder = ",".join(["?"] * len(server_ids))
			raw_res = cursor.execute(f"SELECT * FROM tasks WHERE id IN ({placeholder})", tuple(server_ids)).fetchall()
			res = [list(res) for res in raw_res]
			return JSONResponse({"opr": 0, "data": res})
		else:
			return JSONResponse({"opr": 0, "data": []})
	
	elif req["task"] == "push":
		if req["phase"] == 1:
			client_ids = ids_function("c2s", req["data"])
			return JSONResponse({"opr": 0, "data": client_ids})
		else:
			data = [tuple(row) for row in req["data"]]
			if data:
				cursor.executemany(f"""
					INSERT INTO tasks (
					id,
					title, 
					tags,
					due,
					note,
					status,
					timestamp
					) VALUES (
					?, ?, ?, ?, ?, ?, ?
					)	ON CONFLICT(id)
					DO UPDATE SET
					title = excluded.title,
					tags = excluded.tags,
					due = excluded.due,
					note = excluded.note,
					status = excluded.status,
					timestamp = excluded.timestamp
				""", data)
				if cursor.rowcount > 0:
					conn.commit()
					return JSONResponse({"opr": 0})
				else:
					return JSONResponse({"opr": 1})
	elif req["task"] == "match":
		if req["phase"] == 1:
			server_ids = ids_function("s2c", req["data"])
			client_ids = ids_function("c2s", req["data"])
			
			if server_ids:
				placeholder = ",".join(["?"] * len(server_ids))
				raw_res = cursor.execute(f"SELECT * FROM tasks WHERE id IN ({placeholder})", tuple(server_ids)).fetchall()
				res = [list(row) for row in raw_res]
				conn.commit()
				return JSONResponse({"opr": 0, "ids": client_ids, "data": res})
		else:
			data = [tuple(row) for row in req["data"]]
			if data:
				cursor.executemany(f"""
					INSERT INTO tasks (
					id,
					title, 
					tags,
					due,
					note,
					status,
					timestamp
					) VALUES (
					?, ?, ?, ?, ?, ?, ?
					) ON CONFLICT(id)
					DO UPDATE SET
					title = excluded.title,
					tags = excluded.tags,
					due = excluded.due,
					note = excluded.note,
					status = excluded.status,
					timestamp = excluded.timestamp
				""", data)
				if cursor.rowcount > 0:
					conn.commit()
					return JSONResponse({"opr": 0})
				else:
					return JSONResponse({"opr": 1})
	
	elif req["task"] == "add":
		try:
			if req["specific_task"] == "change_status":
				cursor.execute(f"UPDATE tasks SET status = ?, timestamp = {ctime} WHERE id = ?", tuple(req["data"]))
				if cursor.rowcount > 0:
					conn.commit()
					return JSONResponse({"opr": 0})
				else:
					return JSONResponse({"opr": 1, "desc": "No changes occured in Database"})
			elif req["specific_task"] == "add_task":
				cursor.execute(f"INSERT INTO tasks (id, title, tags, due, note, status, timestamp) VALUES (?, ?, ?, ?, ?, ?, {ctime})", tuple(req["data"]))
				if cursor.rowcount > 0:
					conn.commit()
					return JSONResponse({"opr": 0})
				else:
					return JSONResponse({"opr": 1, "desc": "No changes occured in Database"})
			elif req["specific_task"] == "update_task":
				cursor.execute(f"UPDATE tasks SET title = ?, tags = ?, due = ?, note = ?, timestamp = {ctime} WHERE id = ?", tuple(req["data"]))
				if cursor.rowcount > 0:
					conn.commit()
					return JSONResponse({"opr": 0})
				else:
					return JSONResponse({"opr": 1, "desc": "No changes occured in Database"})
			else:
				return JSONResponse({"opr": 1, "desc": "Invalid Add Request"})
		except:
			return JSONResponse({"opr": 1, "desc": "Error While Inserting Data into Database"})
	
	elif req["task"] == "fetch":
		try:
			data = cursor.execute("SELECT * FROM tasks WHERE id = ?", tuple(req["id"])).fetchone()
			if data is not None:
				return JSONResponse({
					"opr": 0, "data": {
						"id": data[0],
						"title": data[1],
						"tags": json.loads(data[2]) if data[2] != "-" else [],
						"due": data[3],
						"note": data[4],
						"status": data[5]
					}
				})
			else:
				return JSONResponse({"opr": 1, "desc": "No Task for with this Id"})
		except:
			return JSONResponse({"opr": 1, "desc": "Error While Retrieving Data from Database"})
	
	elif req["task"] == "init_data":
		try:
			raw_data = cursor.execute("SELECT id, status, title, tags FROM tasks").fetchall()
			if len(raw_data) > 0:
				data = [{
					"id": row[0],
					"status": True if row[1] else False,
					"title": row[2],
					"tags": json.loads(row[3]) if row[3] != "-" else []
				} for row in raw_data]
				return JSONResponse({"opr": 0, "data": data})
			
			else:
				return JSONResponse({"opr": 1, "desc": "Database is Empty"})
		except:
			return JSONResponse({"opr": 1, "desc": "Error While Retrieving Data from Database"})
	elif req["task"] == "search":
		try:
			query = raq["query"]
			placeholder = []
			values = []
			if query["title"] != "":
				placeholder.append("title LIKE ?")
				values.append(f"%{query["title"]}%")
			if query["tags"] != "":
				tag_placeholder = [f"""
					EXISTS (
						SELECT 1 FROM json_each(tasks.tags)
						WHERE value = ?
					)
				""" for tag in json.loads(query["tags"])]
				placeholder.append(f"(json_valid(tags) AND ({" OR ".join(tag_placeholder)})")
				values.extend(json.load(query["tags"]))
			if query["status"] is not None:
				placeholder.append("status = ?")
				values.append(True if query["status"] else False)
		
		except:
			return JSONResponse({"opr": 1, "desc": "Error while Searching For Task"})
	
	else:
		return JSONResponse({"opr": 1, "desc": "Invalid Request"})


@app.on_event("shutdown")
def on_shutdown():
	conn.commit()
	conn.close()
	print("\033[32mINFO\033[0m:     Database Closed Successfully...")
