structure DTOrderTool = struct
  local
    val tool = "datatype-order"
    val class = "datatype-order"

    val suffixes = ["ord"]
    val replacements = [
      ("sml", SOME "sml", Fn.id)
    ]

    val cmd = "../tools/dt-order"
    val opts = []
    val template = SOME "%c %s > %t"
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
    (*val _ = #set (NowebTool.lineNumbering class) (SOME "(*#line %-1L \"%F\"*)%N")*)
  end
end
