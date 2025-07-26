<h1>Flask Todo App</h1>

<p>A simple Todo List application built with Flask, MongoDB, and Flask-WTF.</p>

<h2>📚 Features</h2>
<ul>
  <li>Add, update, and delete todo items</li>
  <li>Store data in MongoDB</li>
  <li>Use Flask-WTF forms for validation</li>
  <li>Deployed on <strong>Render</strong> using Gunicorn</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
flaskmongodb/
│
├── application/
  ├── __init__.py         ← Initializes Flask app and MongoDB
  └── routes.py
    ├── templates/              ← Jinja2 HTML templates
    ├── view_todos.html
    ├── add_todo.html
    └── layout.html         
  └── forms.py
├── run.py                  ← Entry point for running the app
├── requirements.txt        ← Python package dependencies

</pre>

<h2>🚀 How to Deploy on Render</h2>

<ol>
  <li>Push your code to a GitHub repository</li>
  <li>Go to <a href="https://render.com">Render.com</a> and create a new Web Service</li>
  <li>Connect your GitHub repo</li>
  <li>Set build command: <code>pip install -r requirements.txt</code></li>
  <li>Set start command: <code>gunicorn run:app</code></li>
  <li>Select runtime: Python 3.11 (or latest available)</li>
</ol>

<h3>Environment Variables (if needed)</h3>
<p>Set your MongoDB connection string as an environment variable named <code>MONGO_URI</code>.</p>

<h2>▶️ Run Locally</h2>
<pre>
pip install -r requirements.txt
python run.py
</pre>

<h2>📽️ Learning Source</h2>
<p>This project was created by following the YouTube tutorial playlist: 
<a href="https://www.youtube.com/watch?v=tNDq3JcCh_o&list=PLU7aW4OZeUzwN0TsZLZUuzhc0f7OVVBcT">Flask + MongoDB Playlist</a></p>
