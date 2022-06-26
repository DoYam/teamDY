import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css'

function App() {
  const [rooms, setRooms] = useState([])
  const [check, setCheck] = useState(0)
  const roomTitle = useRef(null)
  const roomPatchTitle = useRef(null)

  // GET: 전체 방 조회
  useEffect(() => {
    axios.get('http://localhost:8000/room/')
    .then((response) => {
      setRooms(response.data);
    })
    .catch(console.log('error!'))
  }, [check])

  const room_list = []
  for(let i = 0; i < rooms.length; i++) {
    room_list.push(
      <div key={i}>
        <h2>{rooms[i].title}</h2>
        <p>{rooms[i].start_date}</p>
      </div>
    )
  }

  // POST: 새로운 방 등록 -> DB에 저장
  const postRoom = () => {
    axios.post('http://localhost:8000/room/', {
      title: roomTitle.current.value,
    })
    .then((response) => {
      setCheck(check + 1);
      roomTitle.current.value = ''
    })
    .catch(console.log('error!'))
  }

  // PATCH: 기존 방 이름 수정
  const room_patch_list = []
  for(let i = 0; i < rooms.length; i++) {
    room_patch_list.push(
      <div key={i}>
        <h2>{rooms[i].title}</h2>
        <p>{rooms[i].start_date}</p>
        <input ref={roomPatchTitle} type="text" placeholder="수정할 방 이름을 입력해주세요"></input>
        <button onClick={() => {
          axios.patch(`http://localhost:8000/room/${rooms[i].id}/`, {
            title: roomPatchTitle.current.value
          })
          .then((response) => {setCheck(check + 1)})
          .catch(console.log('error!'))}}
        >수정하기</button>
      </div>
    )
  }

  // DELETE: 방 삭제
  const room_delete_list = []
  for(let i = 0; i < rooms.length; i++) {
    room_delete_list.push(
      <div key={i}>
        <h2>{rooms[i].title}</h2>
        <p>{rooms[i].start_date}</p>
        <button onClick={() => {
          axios.delete(`http://localhost:8000/room/${rooms[i].id}/`)
          .then((response) => {setCheck(check + 1)})
          .catch(console.log('error!'))}}
        >삭제하기</button>
      </div>
    )
  }

  return (
    <div className="App">
      <div id="getArea">
        <h1>GET</h1>
        {room_list}
      </div>
      <div id="postArea">
        <h1>POST</h1>
        <input ref={roomTitle} type="text" placeholder="저장할 방 이름을 입력해주세요"></input>
        <button onClick={postRoom}>POST</button>
      </div>
      <div id="patchArea">
        <h1>PATCH</h1>
        {room_patch_list}
      </div>
      <div id="deleteArea">
        <h1>DELETE</h1>
        {room_delete_list}
      </div>
    </div>
  );
}

export default App;
