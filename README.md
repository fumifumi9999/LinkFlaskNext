This is a Flask-Next.js repo

### コマンド
- git clone https://github.com/fumifumi9999/LinkFlaskNext.git
- git checkout MySql ※こっちのブランチに変更しないとMySQL用のコードは見れない

■ Tips
- MySQLがどうなっているかを確認する場合はMySQL Workbench等を使用する (SELECT * FROM your-table-nameでほとんどの確認はできます)
- FlaskのAPI動作が怪しい場合は、Insomnia等でFlask単体の動作が期待通りできているか確認する
- Terminalは二つ起動し、frontendの起動とbackendの起動を同時に行う

■ backend ※注意：python 3.11.7推奨（3.12では動かない）
- cd backend
- python3 -m venv backend_env
- ./backend_env/Script/activate.ps1 (powershellの場合)
- pip install -r requirements.txt
- /backend/db_control/.env の作成
- crud.pyの以下をコメント外す
-- # from db_control import create_tables # 初回だけコメントアウトを消す
- flask --app app run
- crud.pyの以下をコメントアウト
-- from db_control import create_tables # 初回だけコメントアウトを消す
- flask --app app run

■ .env内容
- PORT=3306
- DB_USER=your-mysql-username
- PASSWORD=your-mysql-password
- HOST=your-host-name (例：***.mysql.database.azure.com）
- DATABASE=your-db-name

■ frontend
- cd frontend
- npm install
- npm run dev

■ http://localhost:3000/customers にアクセス