# 精选计算机科学课程

一份经人工策展的计算机科学课程与配套教材索引,以"少而精"为原则:条目优先收录完整的教学材料、稳定的链接,以及具有长期学习价值的内容。

> 英文版请见 [README.md](README.md)。

## 目录

> 章节内容位于本文;以下目录链接到英文 [README.md](README.md) 的同名章节,以兼容 GitHub 的非 ASCII 标题锚定规则。

- [编程与基础](README.md#foundations-and-programming)
- [计算机数学](README.md#mathematics-for-computer-science)
- [数据结构与算法](README.md#data-structures-and-algorithms)
- [计算机体系结构与系统](README.md#computer-architecture-and-systems)
- [操作系统](README.md#operating-systems)
- [计算机网络与分布式系统](README.md#computer-networks-and-distributed-systems)
- [数据库与数据管理](README.md#databases-and-data-management)
- [编程语言与编译器](README.md#programming-languages-and-compilers)
- [计算理论](README.md#theory-of-computation)
- [安全与密码学](README.md#security-and-cryptography)
- [人工智能、机器学习与自然语言处理](README.md#artificial-intelligence-machine-learning-and-nlp)
- [计算机视觉、图形学、人机交互与机器人](README.md#computer-vision-graphics-hci-and-robotics)
- [数据科学、并行计算与 Web 开发](README.md#data-science-parallel-computing-and-web-development)
- [教材与配套资源](README.md#texts-and-companion-resources)

## 如何使用本列表

从与你当前水平匹配的 `Intro`(入门) 与 `Core`(核心) 条目开始;当你希望深入或学习历史上有重要意义的课程时,再进入 `Advanced`(进阶) 或 `Archived`(归档) 部分。最后的"教材"一节收录与主课程搭配良好的书籍与课程配套资源。

## 收录标准

- 优先使用第一方链接:大学官方页面、官方课程站点,或官方配套站点。当某个官方课程站点已不再提供访问时,`Archived` 条目可以使用一份对该官方站点的可信归档。
- 同一课程系列仅保留一个权威条目;若归档版本是最可靠的来源,则将其标注为 `Archived`。
- 每门课程在与其学习目标最契合的学科下仅出现一次;教材与项目类资源统一放在最后一节。

## 贡献

欢迎提交课程新增、链接修复、课程元数据更正以及其他语言翻译。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md),并使用 [Pull Request 模板](.github/pull_request_template.md) 提供来源证据与校验结果。翻译文件请使用 `README.<locale>.md` 命名,并与英文 README 的章节结构和课程链接保持一致;新增课程应先同步到英文目录。

## 编程与基础

- [CS50x:计算机科学导论](https://cs50.harvard.edu/x/2026/) - 哈佛大学(入门)。本课程通过习题集与期末项目介绍编程、算法与软件问题求解。
- [MIT 6.100L(原 6.0001):计算机科学与 Python 编程导论](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/) - 麻省理工学院(归档)。2022 年的 OCW 版本通过作业与期末项目教授 Python、计算思维与算法问题求解。
- [UC Berkeley CS61A:计算机程序的构造与解释](https://cs61a.org/) - 加州大学伯克利分校(入门)。本课程通过 Python、Scheme 与 SQL 中的递归、抽象与数据导向编程来建立编程熟练度。
- [Princeton COS 126:计算机科学:跨学科的方法](https://www.cs.princeton.edu/courses/archive/fall26/cos126/) - 普林斯顿大学(入门)。本课程通过讲义、实验与作业介绍编程、数据与计算问题求解。

## 计算机数学

- [UC Berkeley CS70:离散数学与概率论](https://cs70.org/) - 加州大学伯克利分校(核心)。本课程训练后续 CS 理论所需的证明技巧、计数、概率与离散结构。
- [MIT 6.042J:计算机科学数学](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) - 麻省理工学院(归档)。OCW 版本涵盖面向计算的逻辑、证明、图论、计数与离散概率。
- [Stanford CS109:面向计算机科学家的概率论](https://web.stanford.edu/class/cs109/) - 斯坦福大学(核心)。本课程通过习题集与项目教授概率、推断与统计推理。

## 数据结构与算法

- [UC Berkeley CS61B:数据结构](https://fa26.datastructur.es/) - 加州大学伯克利分校(核心)。本课程通过大型项目教授数据结构、算法分析与 Java 编程。
- [MIT 6.006:算法导论](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - 麻省理工学院(归档)。OCW 版本涵盖算法设计、图算法、动态规划与复杂度分析。
- [MIT 6.046J:算法设计与分析](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/) - 麻省理工学院(归档)。OCW 版本进一步深入贪心方法、网络流、随机算法与复杂度。
- [Princeton COS 226:算法与数据结构](https://www.cs.princeton.edu/courses/archive/fall26/cos226/) - 普林斯顿大学(核心)。本课程将数据结构实现与算法设计、分析相结合。
- [UIUC CS225:使用 C++ 的数据结构与算法导论](https://courses.grainger.illinois.edu/cs225/fa2026/) - 伊利诺伊大学香槟分校(核心)。本课程以 C++ 教授链表结构、树、哈希表、图与算法问题求解。

## 计算机体系结构与系统

- [UC Berkeley CS61C:计算机体系结构的伟大思想](https://cs61c.org/) - 加州大学伯克利分校(核心)。本课程从 C 与汇编出发,逐步覆盖缓存、流水线与并行性能。
- [MIT 6.004:计算结构](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) - 麻省理工学院(归档)。OCW 版本从门电路出发,梳理数字逻辑、时序电路与处理器设计。
- [CMU 15-213:计算机系统导论](https://www.cs.cmu.edu/~213/) - 卡内基梅隆大学(核心)。本课程在系统导向的实验序列中串联 C、汇编、链接、内存与性能。
- [ETH Zurich 数字设计与计算机体系结构](https://safari.ethz.ch/ddca/spring2026/doku.php?id=start) - 苏黎世联邦理工学院(核心)。本课程通过实验与练习教授数字逻辑、处理器设计以及硬件/软件边界。
- [CMU 18-447:计算机体系结构导论](https://www.ece.cmu.edu/~ece447/) - 卡内基梅隆大学(归档)。归档的 2024 年春季课程学习流水线、缓存、存储系统与现代处理器设计。

## 操作系统

- [MIT 6.1810(原 6.S081):操作系统工程](https://pdos.csail.mit.edu/6.1810/2025/) - 麻省理工学院(归档)。归档的版本以 xv6 教授进程、虚拟内存、文件系统与并发。
- [UC Berkeley CS162:操作系统与系统编程](https://cs162.org/) - 加州大学伯克利分校(核心)。本课程将操作系统概念与系统编程、同步以及内核抽象相结合。

## 计算机网络与分布式系统

- [MIT 6.5840:分布式系统](https://pdos.csail.mit.edu/6.5840/) - 麻省理工学院(核心)。本课程通过讲义与编程实验研究复制、容错与共识。
- [Stanford CS144:计算机网络](https://web.archive.org/web/20260506063931/https://cs144.github.io/) - 斯坦福大学(归档)。归档的 2025 年秋季课程围绕 TCP/IP 协议栈与可靠传输的实现展开。
- [CMU 15-440:分布式系统](https://www.cs.cmu.edu/~15-440/) - 卡内基梅隆大学(进阶)。本课程研究分布式服务、协调、复制与一致性。

## 数据库与数据管理

- [CMU 15-445/645:数据库系统导论](https://15445.courses.cs.cmu.edu/) - 卡内基梅隆大学(核心)。本课程通过实现型实验覆盖存储引擎、索引、查询处理与事务。
- [CMU 15-721:高级数据库系统](https://15721.courses.cs.cmu.edu/) - 卡内基梅隆大学(归档)。归档的 2025 年秋季课程探讨高级存储、并发、优化与分布式数据系统。

## 编程语言与编译器

- [MIT 6.1100(原 6.035):计算机语言工程](https://6110-sp25.github.io/) - 麻省理工学院(归档)。归档的 2025 年春季课程通过解析、语义分析、优化与代码生成构建一条完整的编译器流水线。
- [Stanford CS143:编译器](https://web.stanford.edu/class/cs143/) - 斯坦福大学(进阶)。本课程覆盖编译器前端、中间表示、优化与运行时支持。

## 计算理论

- [Stanford CS103:计算的数学基础](https://web.stanford.edu/class/cs103/) - 斯坦福大学(核心)。本课程教授计算机科学所需的证明、逻辑、组合与可计算性基础。

## 安全与密码学

- [MIT 6.858:计算机系统安全](https://css.csail.mit.edu/6.858/2022/) - 麻省理工学院(归档)。归档的课程通过讲义、实验与项目覆盖漏洞、防御与系统安全。
- [Stanford CS155:计算机与网络安全导论](https://cs155.stanford.edu/) - 斯坦福大学(进阶)。本课程研究密码学基础、网络攻击与安全系统设计。

## 人工智能、机器学习与自然语言处理

- [CS50 的人工智能导论(Python 版)](https://cs50.harvard.edu/ai/) - 哈佛大学(核心)。本课程通过 Python 项目介绍搜索、优化、机器学习与神经网络方法。
- [Stanford CS221:人工智能:原理与技术](https://cs221.stanford.edu/) - 斯坦福大学(进阶)。本课程综述经典人工智能中的搜索、概率推理、规划与学习。
- [Stanford CS229:机器学习](https://web.stanford.edu/class/cs229/) - 斯坦福大学(进阶)。本课程构建监督学习、优化与机器学习的概率模型。
- [UC Berkeley CS188:人工智能导论](https://inst.eecs.berkeley.edu/~cs188/fa26/) - 加州大学伯克利分校(核心)。本课程覆盖搜索、对抗推理、概率推断与强化学习。
- [UC Berkeley CS189:机器学习导论](https://eecs189.org/) - 加州大学伯克利分校(进阶)。本课程对现代学习方法、泛化与优化进行数学化处理。
- [Stanford CS224N:基于深度学习的自然语言处理](https://web.stanford.edu/class/cs224n/) - 斯坦福大学(进阶)。本课程讲授基于词嵌入、序列模型与 Transformer 的自然语言处理。
- [Stanford CS336:从零开始构建语言模型](https://cs336.stanford.edu/) - 斯坦福大学(进阶)。本课程研究分词器设计、Transformer、训练与语言模型评估。

## 计算机视觉、图形学、人机交互与机器人

- [UC Berkeley CS184/284A:计算机图形学](https://cs184.eecs.berkeley.edu/fa26) - 加州大学伯克利分校(进阶)。本课程通过编码作业与期末项目培养渲染、几何处理与动画能力。
- [Stanford CS231N:用于视觉识别的卷积神经网络](https://cs231n.stanford.edu/) - 斯坦福大学(进阶)。本课程覆盖图像分类、检测与深度视觉模型。

## 数据科学、并行计算与 Web 开发

- [CS50 的 Python 与 JavaScript Web 编程](https://cs50.harvard.edu/web/) - 哈佛大学(核心)。本课程使用 Django、SQL、API 与 JavaScript 构建全栈 Web 应用。
- [Stanford CS149:并行计算](https://cs149.stanford.edu/) - 斯坦福大学(归档)。归档的课程研究并行算法、GPU 编程与性能调优。

## 教材与配套资源

- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) - 教材(核心)。这本免费教材覆盖虚拟化、并发与持久化。
- [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/) - 教材(核心)。配套站点自顶向下地讲解网络,从应用层一路到底层链路。
- [Designing Data-Intensive Applications](https://dataintensive.net/) - 教材(进阶)。官方配套站点跟踪数据模型、复制、分区与流处理。
- [Nand2Tetris](https://www.nand2tetris.org/) - 项目(核心)。该项目从 NAND 门开始,经由编译器与操作系统构建一套完整的计算机系统。
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) - 项目(核心)。这门课程形态的项目讲解 Shell 工具、Git、编辑器、调试与自动化。

## 许可证

本仓库的策展文字以 [CC0 1.0 Universal](LICENSE) 放弃版权;链接到的课程材料仍受其各自来源的许可证约束。
