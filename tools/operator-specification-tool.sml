structure TygenTool = struct
  local
    val tool = "typechecker-generator"
    val class = "operator-specification"

    val suffixes = ["ty"]
    val replacements = [
      ("ord",        SOME "datatype-order", Fn.id),
      ("exp.ord",    SOME "datatype-order", Fn.id),
      ("exp.sml",    SOME "sml",            Fn.id),
      ("exp.sig",    SOME "sml",            Fn.id),
      ("sx.sml",     SOME "sml",            Fn.id)
      (* this is OLC stuff
      ("create.sig", SOME "sml",            Fn.id),
      ("create.sml", SOME "sml",            Fn.id),
      ("check",      SOME "sml",            Fn.id) *)
    ]

    val cmd = "tygen"
    val opts = []
    val template = SOME "%c %s"
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
