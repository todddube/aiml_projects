# how to -
## Start Py Env
 -  ```.\.venv\Scripts\activate```

[Refence run llama locally ollama](https://www.datacamp.com/tutorial/run-llama-3-locally)

# pip upgrade packages
- https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/
- ```pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}```