structure EBNFTool = struct
  local
    val tool = "ebnf"
    val class = "ebnf"

    val suffixes = ["g"]
    val replacements = [
      ("sml", SOME "sml", Fn.id),
      ("tab", SOME "sml", Fn.id)
    ]

    val cmd = "ebnf"
    val opts = ["-picky", "-ml", "-flatten", "-parser"]
    val template = SOME "%c %u %s > %1t && mv ii.tab.sml %2t"
  in
    val _ = Tools.registerStdShellCmdTool {
      tool = tool,
      class = class,
      cmdStdPath = fn () => (cmd, opts),
      template = template,
      extensionStyle = Tools.EXTEND replacements,
      dflopts = []
    }
    val _ = app (fn s => Tools.registerClassifier (Tools.stdSfxClassifier { sfx = s, class = class })) suffixes
    val _ = #set (NowebTool.lineNumbering class) (SOME "#line %L \"%F\"%N")
  end
end
