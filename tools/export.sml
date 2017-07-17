(* give this file to sml to create sml-nw, e.g., sml < export.sml *)
val _ = Compiler.Control.MC.matchNonExhaustiveError := true;
val _ = Compiler.Control.MC.bindContainsVar := false;
(*#line 5 "mkdir.nw"*)signature MKDIR = sig
  val mkdir : {path:string, verbose:bool} -> unit
end
(*#line 9 "mkdir.nw"*)structure Mkdir :> MKDIR = struct
    structure P = OS.Path
    structure F = OS.FileSys
    fun isdir d = F.isDir d handle OS.SysErr _ => false
    fun mkdir {path, verbose} =
      let fun mk "" = ()
            | mk dir = F.mkDir dir handle _ => 
                         (mk (#dir (P.splitDirFile dir)); F.mkDir dir)
      in  if isdir path then ()
          else ( if verbose then app print ["[Creating directory ", path, " ...]\n"]
		 else ()
	       ; mk path
	       )
      end
end
(*#line 39 "nwsource.nw"*)signature NOWEB_SOURCE = sig
  type class = string
  val registerLineNumbering : class * string option -> string option
     (* returns old numbering *)
  val alwaysOverwrite : bool ref
  val derivedDirectory : string option ref
end
(*#line 48 "nwsource.nw"*)functor NowebSourceFun (structure Tools: CMTOOLS) : NOWEB_SOURCE = struct
  local
    val notangle = "notangle -t"
    val class = "noweb"
    val alwaysOverwrite = ref false
    fun child (file, dirpath) = OS.Path.joinDirFile {dir=dirpath, file=file}
(*val derivedDirectory = ref (SOME(foldl child OS.Path.currentArc ["CM", "derived"]))*)
    val derivedDirectory = ref (SOME(foldl child OS.Path.currentArc ["NW"]))

    fun derived file =
      case !derivedDirectory
	of NONE => file
	 | SOME d => OS.Path.concat(d, file)

    
(*#line 147 "nwsource.nw"*)fun split_at name =
  let fun split (pre, #"@" :: post) = (SOME (implode (rev pre)), implode post)
        | split (pre, c    :: post) = split(c::pre, post)
        | split (pre, [])           = (NONE, implode (rev pre))
  in  split([], explode name)
  end
(*#line 155 "nwsource.nw"*)fun remove_extension (name, ext') =
  let val {base, ext} = OS.Path.splitBaseExt name
  in  if ext = SOME ext' then base else name
  end
(*#line 63 "nwsource.nw"*)    fun rule name =
      let val (pre, post) = split_at name
          val base = remove_extension(post, "nw")
          fun join ext = OS.Path.joinBaseExt{base=base, ext=SOME ext}
          fun d l = map (fn (f, ?) => (derived f, ?)) l
      in  case pre
            of NONE => d [(join "sml", SOME "sml"), (join "sig", SOME "sml")]
             | SOME prefix => d [(prefix, NONE)]
      end
  
    fun validator {source, targets} = 
      Tools.stdTStampValidator {source = #2 (split_at source), targets=targets}
  
    
(*#line 131 "nwsource.nw"*)local
  val lineNumberings = ref [("sml", SOME "(*#line %L \"%F\"*)")]
in
  fun lineNumbering class =
    let fun l [] = NONE
          | l ((c, n)::t) = if class = c then n else l t
    in  l (!lineNumberings)
    end
  fun registerLineNumbering (class, numbering) =
    let val old = lineNumbering class
    in  lineNumberings := (class, numbering) :: !lineNumberings;
        old
    end
end

(*#line 78 "nwsource.nw"*)    fun extract_file (source, (fulltarget, class)) =
      let val (_, srcFile) = split_at source
	  val target = OS.Path.file fulltarget
          val class = case class of SOME c => class
                                  | NONE   => Tools.defaultClassOf target
	  val numbering = case class of NONE => NONE | SOME c => lineNumbering c
          val format_option = case numbering
                                of NONE     => ""
                                 | SOME fmt => concat ["-L'", fmt, "'"]
          val overwrite = if !alwaysOverwrite then ">" else "| cpif"
          val cmd = concat [notangle, " ", format_option, " -R'", target, "' ", 
                            srcFile, " ", overwrite, " ", fulltarget]
          val _ = app print ["[", cmd, "]\n"]
          val _ = case !derivedDirectory
	            of SOME d => Mkdir.mkdir {path=d, verbose=true}
		     | NONE => ()
      in
          if (OS.Process.system cmd) = OS.Process.success then ()
          else (
            OS.FileSys.remove fulltarget;
            raise Tools.ToolError { tool = "Noweb", msg = cmd }
          )
      end

    fun processor {source, targets} =
      let fun process target = 
            if validator {source=source, targets=[target]} then 
              ()
            else 
              extract_file(source, target)
      in  app process targets
      end
  
    fun sfx s = Tools.addClassifier 
                      (Tools.stdSfxClassifier { sfx = s, class = class })
  in
    val _ = Tools.addToolClass { class = class,
                           	 rule = Tools.dontcare rule,
                                 validator = validator,
                           	 processor = processor }
    val _ = sfx "nw"
    val alwaysOverwrite = alwaysOverwrite
    val derivedDirectory = derivedDirectory
    val registerLineNumbering = registerLineNumbering
    type class = string
  end
end
(*#line 161 "nwsource.nw"*)structure NowebSource : NOWEB_SOURCE = NowebSourceFun (structure Tools = CM.Tools)
(*#line 5 "tygensource.nw"*)functor TygenSourceFun (structure Tools: CMTOOLS) = struct
  local
    val command = "tygen"

    val class = "operator-specification"

    fun rule name =
      let fun join ext = OS.Path.joinBaseExt{base=name, ext=SOME ext}
      in  [ (join "ord", SOME "datatype-order")
	  , (join "exp.ord", SOME "datatype-order")
	  , (join "exp.sml", SOME "sml")
	  , (join "exp.sig", SOME "sml")
	  , (join "sx.sml",  SOME "sml")
(******** this is OLC stuff 
	  , (join "create.sig", SOME "sml")
	  , (join "create.sml", SOME "sml")
	  , (join "check", SOME "sml")
******)
	  ]
      end
  
    val validator = Tools.stdTStampValidator

    fun processor {source, targets} =
      let val cmd = concat [command, " ", source]
          val _ = app print ["[", cmd, "]\n"]
      in
          if (OS.Process.system cmd) = OS.Process.success then
	    ()
          else (
            app (fn (file, _) => OS.FileSys.remove file) targets;
            raise Tools.ToolError { tool = "typechecker-generator", msg = cmd }
          )
      end
  
    fun sfx s = Tools.addClassifier 
                      (Tools.stdSfxClassifier { sfx = s, class = class })
  in
    val _ = Tools.addToolClass { class = class : Tools.class,
                           	 rule = Tools.dontcare rule : Tools.rule,
                                 validator = validator,
                           	 processor = processor : Tools.processor }
    val _ = sfx "ty"
    val _ = NowebSource.registerLineNumbering(class, SOME "#line %L \"%F\"%N")
  end
end
(*#line 52 "tygensource.nw"*)structure TygenSource = TygenSourceFun(structure Tools = CM.Tools);
(*#line 3 "ebnfsource.nw"*)functor EBNFSourceFun (structure Tools: CMTOOLS) = struct
  local
    val command = "ebnf -picky -ml -flatten -parser"

    val class = "ebnf"

    fun rule name =
      let val parser = OS.Path.joinBaseExt {base=name, ext=SOME "sml"}
          val tokens = OS.Path.joinBaseExt {base=name, ext=SOME "tab"}
      in  [(parser, SOME "sml"), (tokens, SOME "sml")]
      end
  
    val validator = Tools.stdTStampValidator

    fun processor {source, targets} =
      let val parser = OS.Path.joinBaseExt {base=source, ext=SOME "sml"}
          val tokens = OS.Path.joinBaseExt {base=source, ext=SOME "tab"}
          val cmd = concat [command, " ", source, " > ", parser]
          val _ = app print ["[", cmd, "]\n"]
      in
          if (OS.Process.system cmd) = OS.Process.success then (
	    OS.FileSys.rename {old="ii.tab.sml", new=tokens}
          ) else (
            OS.FileSys.remove parser;
            raise Tools.ToolError { tool = "ebnf", msg = cmd }
          )
      end
  
    fun sfx s = Tools.addClassifier 
                      (Tools.stdSfxClassifier { sfx = s, class = class })
  in
    val _ = Tools.addToolClass { class = class,
                           	 rule = Tools.dontcare rule,
                                 validator = validator,
                           	 processor = processor }
    val _ = sfx "g"
    val _ = NowebSource.registerLineNumbering(class, SOME "#line %L \"%F\"%N")
  end
end
(*#line 43 "ebnfsource.nw"*)structure EBNFSource = EBNFSourceFun(structure Tools = CM.Tools);
(*#line 4 "ordsource.nw"*)functor DTOrderSourceFun (structure Tools: CMTOOLS) = struct
  local
    val command = "dt-order"

    val class = "datatype-order"

    fun rule name =
      let val orderfun = OS.Path.joinBaseExt {base=name, ext=SOME "sml"}
      in  [(orderfun, SOME "sml")]
      end
  
    val validator = Tools.stdTStampValidator

    fun processor {source, targets} =
      let val orderfun = OS.Path.joinBaseExt {base=source, ext=SOME "sml"}
          val cmd = concat [command, " ", source, " > ", orderfun]
          val _ = app print ["[", cmd, "]\n"]
      in
          if (OS.Process.system cmd) = OS.Process.success then
	    ()
          else (
            OS.FileSys.remove orderfun;
            raise Tools.ToolError { tool = "datatype-order", msg = cmd }
          )
      end
  
    fun sfx s = Tools.addClassifier 
                      (Tools.stdSfxClassifier { sfx = s, class = class })
  in
    val _ = Tools.addToolClass { class = class,
                           	 rule = Tools.dontcare rule,
                                 validator = validator,
                           	 processor = processor }
    val _ = sfx "ord"
(*  val _ = NowebSource.registerLineNumbering(class, SOME "(*#line %-1L \"%F\"*)%N") *)
  end
end
(*#line 42 "ordsource.nw"*)structure DTOrderSource = DTOrderSourceFun(structure Tools = CM.Tools);
(*#line 4 "lex+source.nw"*)functor LexSourceFun (structure Tools: CMTOOLS
		      val command: string) =
struct

    local
	val runlex =
	    Tools.stdShellProcessor 
               ( { mkCommand = fn () => command, tool = "ML-Lex+" }  (* new style *)
               ; { command = command, tool = "ML-Lex+" }  (* old style *)
               )
	fun rule source = let
	    val smlfile = source ^ ".sml"
	in
	    [(smlfile, SOME "sml")]
	end

	val validator = Tools.stdTStampValidator

	val processor = runlex

	(* install MlLex class *)
	open Tools
	val class = "mllex+"
	fun sfx s = addClassifier (stdSfxClassifier { sfx = s, class = class })
    in
	val _ = addToolClass { class = class,
			       rule = dontcare rule,
			       validator = validator,
			       processor = processor }
	val _ = sfx "lex+"
	val _ = sfx "l+"
    end
end
(*#line 38 "lex+source.nw"*)structure LexPlusSource = 
  LexSourceFun(structure Tools = CM.Tools val command = "ml-lex+");
val cd = OS.FileSys.chDir
fun build s = (CM.recompile' (s ^ ".cm") before
               print "<======= *NOT* CM.make() ========>\n")
fun mkAll _ = 
  let val flag = NowebSource.alwaysOverwrite
      val old = !flag
      val oldGoing = CM.keep_going (SOME true)
      fun reset () = (flag := old; CM.keep_going (SOME oldGoing); ())
  in  (flag := true; CM.make(); reset()) handle e => (reset(); raise e)
  end;
fun buildAll s = 
  let val flag = NowebSource.alwaysOverwrite
      val old = !flag
      val oldGoing = CM.keep_going (SOME true)
      fun reset () = (flag := old; CM.keep_going (SOME oldGoing); ())
  in  (flag := true; build s; reset()) handle e => (reset(); raise e)
  end;

val _ = (SMLofNJ.exportML "sml-nw"; print Compiler.banner;
         print " [CM+nw+tygen+ebnf+ord+lex+]\n");
