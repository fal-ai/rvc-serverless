# Run Mangio-RVC-Fork on fal

Install fal-serverless and authenticate.

From inside this repository run:

```
fal-serverless function serve app.py app --alias myrvc --auth public
```

This will return a URL and you can navigate to this URL and access the Mangio-RVC gradio app.

You can trigger inference and training, but will see an error, because fal does not allow web socket connections yet.

With public auth, anyone with the app url can use and spend your money. To disable public auth, you can run:

```
fal-serverless function serve app.py app --alias myrvc --auth private
```
