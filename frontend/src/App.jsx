import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [users, setUsers] = useState(null)
  const [posts, setPosts] = useState(null)
  const [deletedPosts, setDeletedPosts] = useState(null)

  async function GetUsers() {
    fetch('http://localhost:8000/users').then((response) => response.json()).then((json) => setUsers(json));
  }

  async function GetPosts() {
    fetch('http://localhost:8000/posts').then((response) => response.json()).then((json) => setPosts(json));
  }

  async function GetDeletedPosts() {
    fetch('http://localhost:8000/posts/deleted').then((response) => response.json()).then((json) => setDeletedPosts(json));
  }

  useEffect(() => {
    GetUsers();
    GetPosts();
    GetDeletedPosts();
  }, []);

  return (
    <>
      <div>
        <table>
          <thead>
            <tr>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>ID</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Username</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Description</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Created At</td>
            </tr>
          </thead>
          <tbody>
            {
              users?.map((u) =>
                <tr key={u.id}>
                  <td style={{ padding: "4px 10px" }}>{u.id}</td>
                  <td style={{ padding: "4px 10px" }}>{u.username}</td>
                  <td style={{ padding: "4px 10px" }}>{u.description}</td>
                  <td style={{ padding: "4px 10px" }}>{u.created_at}</td>
                </tr>

              )
            }
          </tbody>
        </table>

        <table>
          <thead>
            <tr>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>ID</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Posted By</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Description</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Created At</td>
              <td style={{ padding: "4px 10px", fontWeight: "bold" }}>Deleted At</td>
            </tr>
          </thead>
          <tbody>
            {
              posts?.map((p) =>
                <tr key={p.id}>
                  <td style={{ padding: "4px 10px" }}>{p.id}</td>
                  <td style={{ padding: "4px 10px" }}>{users?.filter(u => u.id == p.user_id)[0].username}</td>
                  <td style={{ padding: "4px 10px" }}>{p.description}</td>
                  <td style={{ padding: "4px 10px" }}>{p.created_at}</td>
                  <td style={{ padding: "4px 10px" }}>{p.deleted_at}</td>
                </tr>
              )
            }
            {
              deletedPosts?.map((p) =>
                <tr key={p.id}>
                  <td style={{ padding: "4px 10px" }}>{p.id}</td>
                  <td style={{ padding: "4px 10px" }}>{users?.filter(u => u.id == p.user_id)[0].username}</td>
                  <td style={{ padding: "4px 10px" }}>{p.description}</td>
                  <td style={{ padding: "4px 10px" }}>{p.created_at}</td>
                  <td style={{ padding: "4px 10px" }}>{p.deleted_at}</td>
                </tr>
              )
            }
          </tbody>
        </table>
      </div>
    </>
  )
}

export default App
