
OnceID - OnceID implementation for Python

SUMMARY

This package is intended to help those looking for a way to shorten numerical ID
values.

Additionally, it provides a way to generate a random ID -- a OnceID (shameless
plug) -- where uniqueness can be probable, depending on the length of the ID.

Finally, users have access to a core ID generator function. There, they can
specify the length of their IDs, if they do not like the two preset options.

This package DOES NOT and WILL NOT GUARANTEE a unique ID. It can come close, but
it is more of a supplement to truly unique IDs.

BACKGROUND

While I decided to give my particular implementation a name, neither the concept
or the mechanics behind this kind of encoding are mine.

I scratched an itch in Perl and wanted to give it a try in Python; this was
helpful in the end, since one tends to find ways to optimize when working in
a few different languages.

