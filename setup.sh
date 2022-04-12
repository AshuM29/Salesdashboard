mkdir -p ~/.streamlit

echo "\
[general]\n\
email = \"maheshwariashu29@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
global.developmentMode = false\n\
" > ~/.streamlit/config.toml