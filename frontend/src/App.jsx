const BASE = "http://localhost:8000";
import React, { useEffect, useState } from "react";

async function handleRes(res) {
  const text = await res.text();
  let parsed;
  try {
    parsed = text ? JSON.parse(text) : null;
  } catch (e) {
    parsed = text;
  }
  if (!res.ok) {
    const body = typeof parsed === "string" ? parsed : JSON.stringify(parsed);
    throw new Error(`HTTP ${res.status}: ${body}`);
  }
  return parsed;
}

function qParams(obj = {}) {
  const p = new URLSearchParams();
  for (const k in obj) {
    if (obj[k] !== undefined && obj[k] !== null) p.append(k, String(obj[k]));
  }
  return p.toString();
}

// ---- Users ----
async function getUsers(username = null) {
  const url = username ? `${BASE}/users?username=${encodeURIComponent(username)}` : `${BASE}/users`;
  const res = await fetch(url);
  return handleRes(res);
}

async function getUserById(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}`);
  return handleRes(res);
}

async function getFollowers(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}/followers`);
  return handleRes(res);
}

async function getFollowing(follower_id) {
  const res = await fetch(`${BASE}/users/${follower_id}/following`);
  return handleRes(res);
}

async function createUser(username) {
  const res = await fetch(`${BASE}/users?username=${username}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function updateUsername(user_id, username) {
  const res = await fetch(`${BASE}/users/${user_id}?username=${username}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function deleteUser(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}`, { method: "DELETE" });
  return handleRes(res);
}

async function addFollower(user_id, follower_id) {
  const res = await fetch(`${BASE}/users/${user_id}/followers?follower_id=${follower_id}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function removeFollower(user_id, follower_id) {
  const q = qParams({ follower_id });
  const res = await fetch(`${BASE}/users/${user_id}/followers?${q}`, { method: "DELETE" });
  return handleRes(res);
}

// ---- Posts ----
async function getPosts() {
  const res = await fetch(`${BASE}/posts`);
  return handleRes(res);
}

async function getDeletedPosts() {
  const res = await fetch(`${BASE}/posts/deleted`);
  return handleRes(res);
}

async function getPostById(post_id) {
  const res = await fetch(`${BASE}/posts/${post_id}`);
  return handleRes(res);
}

async function getPostsByUser(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}/posts`);
  return handleRes(res);
}

async function getDeletedPostsByUser(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}/posts/deleted`);
  return handleRes(res);
}

async function createPost(user_id, description) {
  const res = await fetch(`${BASE}/users/${user_id}/posts?description=${description}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function updatePostDescription(post_id, description) {
  const res = await fetch(`${BASE}/posts/${post_id}?description=${description}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function deletePost(post_id) {
  const res = await fetch(`${BASE}/posts/${post_id}`, { method: "DELETE" });
  return handleRes(res);
}

// ---- Comments ----
async function getComments() {
  const res = await fetch(`${BASE}/comments`);
  return handleRes(res);
}

async function getDeletedComments() {
  const res = await fetch(`${BASE}/comments/deleted`);
  return handleRes(res);
}

async function getUserComments(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}/comments`);
  return handleRes(res);
}

async function getDeletedUserComments(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}/comments/deleted`);
  return handleRes(res);
}

async function getPostComments(post_id) {
  const res = await fetch(`${BASE}/posts/${post_id}/comments`);
  return handleRes(res);
}

async function getDeletedPostComments(post_id) {
  const res = await fetch(`${BASE}/posts/${post_id}/comments/deleted`);
  return handleRes(res);
}

async function createComment(post_id, user_id, comment) {
  const res = await fetch(`${BASE}/posts/${post_id}/comments?user_id=${user_id}&comment=${comment}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function updateComment(comment_id, comment) {
  const res = await fetch(`${BASE}/comments/${comment_id}?comment=${comment}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function deleteComment(comment_id) {
  const res = await fetch(`${BASE}/comments/${comment_id}`, { method: "DELETE" });
  return handleRes(res);
}

// ---- Favorites ----
async function getFavorites() {
  const res = await fetch(`${BASE}/favorites`);
  return handleRes(res);
}

async function getPostFavorites(post_id) {
  const res = await fetch(`${BASE}/posts/${post_id}/favorites`);
  return handleRes(res);
}

async function getUserFavorites(user_id) {
  const res = await fetch(`${BASE}/users/${user_id}/favorites`);
  return handleRes(res);
}

async function addFavorite(post_id, user_id) {
  const res = await fetch(`${BASE}/posts/${post_id}/favorites?user_id=${user_id}`, {
    method: "POST",
  });
  return handleRes(res);
}

async function removeFavorite(post_id, user_id) {
  const q = qParams({ user_id });
  const res = await fetch(`${BASE}/posts/${post_id}/favorites?${q}`, { method: "DELETE" });
  return handleRes(res);
}

function Loader({ text = "Loading..." }) {
  return <div style={{ padding: 12, color: "#666" }}>{text}</div>;
}

function ErrorBox({ error, onClose }) {
  if (!error) return null;
  return (
    <div style={{ background: "#fee", border: "1px solid #fbb", padding: 8, margin: 8 }}>
      <strong>Error:</strong> {String(error)}
      <button style={{ marginLeft: 8 }} onClick={onClose}>Dismiss</button>
    </div>
  );
}

function UsersList({ onSelect }) {
  const [users, setUsers] = useState(null);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState(null);
  const [username, setUsername] = useState("");

  async function load() {
    setLoading(true);
    setErr(null);
    try {
      const data = await getUsers();
      setUsers(data);
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { load(); }, []);

  async function handleCreate(e) {
    e.preventDefault();
    if (!username.trim()) return;
    try {
      await createUser(username.trim());
      setUsername("");
      await load();
    } catch (e) {
      setErr(e.message);
    }
  }

  return (
    <div style={{ padding: 12 }}>
      <h2>Users</h2>
      <form onSubmit={handleCreate} style={{ display: "flex", gap: 8, marginBottom: 8 }}>
        <input placeholder="new username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <button type="submit">Create</button>
      </form>
      <ErrorBox error={err} onClose={() => setErr(null)} />
      {loading && <Loader />}
      {!loading && users && users.length === 0 && <div>No users yet</div>}
      {!loading && users && (
        <ul style={{ paddingLeft: 0, listStyle: "none" }}>
          {users.map(u => (
            <li key={u.id} style={{ padding: "6px 0", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <button onClick={() => onSelect(u)} style={{ background: "none", border: "none", cursor: "pointer", textAlign: "left" }}>
                <div style={{ fontWeight: 600 }}>@{u.username}</div>
                <div style={{ fontSize: 12, color: "#666" }}>id: {u.id}</div>
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function PostsPanel({ currentUserId }) {
  const [posts, setPosts] = useState(null);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState(null);
  const [desc, setDesc] = useState("");
  const [userIdForNew, setUserIdForNew] = useState(currentUserId || "");

  async function load() {
    setLoading(true);
    setErr(null);
    try {
      const data = await getPosts();
      setPosts(data);
    } catch (e) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { load(); }, []);

  async function handleCreate(e) {
    e.preventDefault();
    if (!userIdForNew || !desc.trim()) return;
    try {
      await createPost(userIdForNew, desc.trim());
      setDesc("");
      await load();
    } catch (e) {
      setErr(e.message);
    }
  }

  async function handleFavorite(postId) {
    try {
      // demo: favorite as user 1 by default if currentUserId not provided
      const userId = currentUserId || 1;
      await addFavorite(postId, userId);
      await load();
    } catch (e) {
      setErr(e.message);
    }
  }

  return (
    <div style={{ padding: 12 }}>
      <h2>Posts</h2>
      <form onSubmit={handleCreate} style={{ display: "flex", gap: 8, marginBottom: 8 }}>
        <input placeholder="user id" value={userIdForNew} onChange={(e) => setUserIdForNew(e.target.value)} style={{ width: 80 }} />
        <input placeholder="description" value={desc} onChange={(e) => setDesc(e.target.value)} style={{ flex: 1 }} />
        <button type="submit">Post</button>
      </form>

      <ErrorBox error={err} onClose={() => setErr(null)} />
      {loading && <Loader />}
      {!loading && posts && posts.length === 0 && <div>No posts yet</div>}
      {!loading && posts && (
        <div>
          {posts.map(p => (
            <div key={p.id} style={{ border: "1px solid #eee", borderRadius: 6, padding: 8, marginBottom: 8 }}>
              <div style={{ fontWeight: 700 }}>@{p.username || p.user_username || "user"}</div>
              <div style={{ marginTop: 6 }}>{p.description}</div>
              <div style={{ marginTop: 8, display: "flex", alignItems: "center", gap: 8 }}>
                <button onClick={() => handleFavorite(p.id)}>Favorite</button>
                <small style={{ color: "#666" }}>post id: {p.id}</small>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function UserDetail({ user, onClose }) {
  const [followers, setFollowers] = useState(null);
  const [following, setFollowing] = useState(null);
  const [posts, setPosts] = useState(null);
  const [err, setErr] = useState(null);
  const [newFollowerId, setNewFollowerId] = useState("");

  async function loadAll() {
    try {
      const [f, g, p] = await Promise.all([
        getFollowers(user.id),
        getFollowing(user.id),
        getPostsByUser(user.id)
      ]);
      setFollowers(f || []);
      setFollowing(g || []);
      setPosts(p || []);
    } catch (e) {
      setErr(e.message);
    }
  }

  useEffect(() => { loadAll(); }, [user]);

  async function handleAddFollower(e) {
    e.preventDefault();
    if (!newFollowerId) return;
    try {
      await addFollower(user.id, newFollowerId);
      setNewFollowerId("");
      await loadAll();
    } catch (e) {
      setErr(e.message);
    }
  }

  async function handleRemoveFollower(followerId) {
    try {
      await removeFollower(user.id, followerId);
      await loadAll();
    } catch (e) {
      setErr(e.message);
    }
  }

  return (
    <div style={{ padding: 12, borderLeft: "1px solid #eee" }}>
      <button onClick={onClose} style={{ marginBottom: 8 }}>&larr; Back</button>
      <h3>@{user.username} (id: {user.id})</h3>
      <ErrorBox error={err} onClose={() => setErr(null)} />

      <section style={{ marginTop: 12 }}>
        <h4>Followers</h4>
        {!followers ? <Loader /> : followers.length === 0 ? <div>No followers</div> :
          <ul style={{ listStyle: "none", paddingLeft: 0 }}>
            {followers.map(f => (
              <li key={f.id} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0" }}>
                <span>@{f.username}</span>
                <button onClick={() => handleRemoveFollower(f.id)}>Remove</button>
              </li>
            ))}
          </ul>
        }

        <form onSubmit={handleAddFollower} style={{ marginTop: 8, display: "flex", gap: 8 }}>
          <input placeholder="follower id" value={newFollowerId} onChange={(e) => setNewFollowerId(e.target.value)} />
          <button type="submit">Add</button>
        </form>
      </section>

      <section style={{ marginTop: 12 }}>
        <h4>Following</h4>
        {!following ? <Loader /> : following.length === 0 ? <div>Not following anyone</div> :
          <ul style={{ listStyle: "none", paddingLeft: 0 }}>
            {following.map(f => <li key={f.id}>@{f.username}</li>)}
          </ul>
        }
      </section>

      <section style={{ marginTop: 12 }}>
        <h4>Posts</h4>
        {!posts ? <Loader /> : posts.length === 0 ? <div>No posts</div> :
          posts.map(p => (
            <div key={p.id} style={{ border: "1px solid #eee", padding: 8, marginBottom: 8 }}>
              <div style={{ fontWeight: 700 }}>{p.description}</div>
              <div style={{ fontSize: 12, color: "#666" }}>post id: {p.id}</div>
            </div>
          ))
        }
      </section>
    </div>
  );
}

export default function App() {
  const [selectedUser, setSelectedUser] = useState(null);
  const [view, setView] = useState("users");

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", minHeight: "100vh", background: "#fafafa" }}>
      <header style={{ background: "#fff", padding: 12, display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "1px solid #eee" }}>
        <h1 style={{ margin: 0 }}>Social Frontend</h1>
        <nav>
          <button onClick={() => { setView("users"); setSelectedUser(null); }} style={{ marginRight: 8 }}>Users</button>
          <button onClick={() => { setView("posts"); setSelectedUser(null); }}>Posts</button>
        </nav>
      </header>

      <main style={{ display: "flex", gap: 12, padding: 12 }}>
        <aside style={{ width: 320, background: "#fff", borderRadius: 6, boxShadow: "0 1px 2px rgba(0,0,0,0.03)" }}>
          <UsersList onSelect={(u) => { setSelectedUser(u); setView("detail"); }} />
        </aside>

        <section style={{ flex: 1, background: "#fff", borderRadius: 6, padding: 12 }}>
          {view === "posts" && <PostsPanel currentUserId={null} />}
          {view === "users" && (
            <div style={{ padding: 12 }}>
              <h2>Welcome</h2>
              <p>Select a user to view details, or switch to Posts to create and favorite posts.</p>
            </div>
          )}
          {view === "detail" && selectedUser && <UserDetail user={selectedUser} onClose={() => { setView("users"); setSelectedUser(null); }} />}
        </section>
      </main>

      <footer style={{ padding: 12, textAlign: "center", color: "#666" }}>
        API base: {import.meta.env.VITE_API_BASE || "http://localhost:8000"}
      </footer>
    </div>
  );
}