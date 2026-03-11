# Overview

This repository contains Python code snippets used to test the “Add superclass constructor call” quick-fix in PyCharm.

The quick-fix is triggered when a subclass overrides the __init__ method but does not call the constructor of its superclass. When invoked (via Alt + Enter or mouse click), the IDE suggests inserting the appropriate super().__init__(...) call.

The purpose of this repository is to provide small, focused Python examples that correspond to the scenarios described in the test plan.

# Test Plan

The functional test plan verifies that the quick-fix:
1. Detects when a subclass overrides __init__ without invoking the superclass constructor.

2. Displays the “Missing superclass constructor call” inspection.

3. Offers the Add superclass constructor call quick-fix.

4. Inserts the correct super().__init__(...) invocation.

5. Preserves Python syntax, semantics, and formatting.

The test cases focus primarily on functional behavior, while also covering several Python language features and edge cases.
### Python version used for execution: 
```
3.14.3
```

### IDE:
```
PyCharm 2025.3.3
Build #PY-253.31033.139, built on February 19, 2026
Runtime version: 21.0.10+7-b1163.108 aarch64 (JCEF 137.0.17)
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Toolkit: sun.lwawt.macosx.LWCToolkit
macOS 26.2
GC: G1 Young Generation, G1 Concurrent GC, G1 Old Generation
Memory: 2048M
Cores: 8
Metal Rendering is ON
```

### To execute:
```
python filename.py
```

