---
cssclasses:
  - cards
  - cards-cover
  - cards-2-3
  - cards-cols-4
  - dataview-cards
dvStatus: ""
dvGenre: ""
dvDate: ""
dvName: ""
---

`INPUT[inlineSelect(defaultValue(unread), option(unread, Unread), option(read, Read), option('', *)):dvStatus]` 

`INPUT[inlineSelect(defaultValue(''), option(2023, 2023), option(2024, 2024), option('', *)):dvDate]` 

`INPUT[inlineSelect(defaultValue(''), option(fantasy, Fantasy), option(science fiction, Science Fiction), option(fiction, Fiction), option(non-fiction, Non-fiction), option('', *)):dvGenre]` 

`INPUT[text(placeholder(Book Name)):dvName]`

```dataview
TABLE WITHOUT ID
  ("![coverimg|100](" + image + ")") AS "Cover",
  choice(!aliases, link(file.link, file.name), link(file.link, aliases)) AS "Title",
  published,
  genre,
  "by " + author AS "Author"
WHERE contains(file.folder, "book_notes") AND contains(lower(file.aliases), lower(this.dvName)) AND contains(string(created.year), string(this.dvDate)) AND startswith(genre, this.dvGenre) AND contains(status, this.dvStatus) AND file.name != this.file.name
SORT file.name ASC
```
