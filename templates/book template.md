<%*
let title = tp.file.title
if (title.startsWith("Untitled")) {
title = await tp.system.prompt("Title");
}
await tp.file.rename(title)
-%>---
type: book
aliases: 
- "& <%* tR += title %>"
cover: {{coverUrl}}
start:
end:
status: todo 
recomendedby:
---
___
tags:: 
prev:: [[books|назад в библиотеку]]
category::
author:: {{author}}
link:: {{ССЫЛКА НА КНИГУ}}.pdf
children::
___
[[../files/{{ССЫЛКА НА КНИГУ}}.pdf|Читать]]
![cover|150]({{coverUrl}})
___

<% tp.file.cursor(0) %>