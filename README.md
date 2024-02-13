# Workspace Automation
A python compiler for automating keyboard actions

## Language
This is how `wsps` (Workspace Script) works:
**Everything is string**

Setup Comment
```text
// This is how comments will define
```

Setup focus window name if this not define script will not wait until windows focused
```text
!#focus: "<FOCUS WINDOW>";
```


Setup delay time (digit as millisecond)
```text
!#delay: "<Delay as millisecond (int)>";
```

Setup shortcut string
```text
!#short: "<SHORTCUT>";
```

Setup phrase that need to be typed!
```text
!#type: "<PHRASE>";
```

VARIABLES:
setup a varialbe:
```text
// !@ <Name> = "<VALUE>";
!@ name = "wsp";
```
Usage:
```text
// !$<Name>;
!$name;
```

print method
```text
!print("<DATA>");
```
