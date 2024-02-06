# while(1){ cat C:\Users\Empitrix\AppData\Local\Programs\WSP\db.json; sleep 1; Clear-Host}
while(1){ cat C:\Users\Empitrix\AppData\Local\Programs\WSP\db.json | jq -C; sleep 1; Clear-Host}
