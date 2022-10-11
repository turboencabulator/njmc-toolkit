structure LexPlusTool = struct
  local
    val tool = "ML-Lex+"
    val class = "mllex+"

    val suffixes = ["lex+", "l+"]
    val replacements = [
      ("sml", SOME "sml", Fn.id)
    ]

    val cmd = "sml"
    val opts = ["@SMLload=../tools/ml-lex+"]
    val template = NONE
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
  end
end
