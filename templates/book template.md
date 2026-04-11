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
cover: ССЫЛКА НА ОБЛОЖКУ
start:
end:
status: todo 
recomendedby:
---
___
tags:: 
prev:: [[books|назад в библиотеку]]
category::
author:: Неизвестный
link:: [[../files/ССЫЛКА НА КНИГУ.pdf|Читать]]
children::
___
![cover|150](coverUrl)
___

<% tp.file.cursor(0) %>