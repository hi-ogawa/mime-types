# mime-types

```sh
# generate files
curl https://hg.nginx.org/nginx/raw-file/release-1.23.1/conf/mime.types | python main.py

# exmple: content-type -> extension
curl https://cdn.jsdelivr.net/gh/hi-ogawa/mime-types/content-types/image/svg+xml
svg

# example: extension -> content-type
curl https://cdn.jsdelivr.net/gh/hi-ogawa/mime-types/extensions/svg
image/svg+xml
```

## references

- https://hg.nginx.org/nginx/file/default/conf/mime.types
