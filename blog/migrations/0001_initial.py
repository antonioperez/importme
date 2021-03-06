# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', tinymce.models.HTMLField()),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('commenter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, to='blog.Comment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=30, choices=[(b'4th Dimension/4D', b'4th Dimension/4D'), (b'ABAP', b'ABAP'), (b'ABC', b'ABC'), (b'ActionScript', b'ActionScript'), (b'Ada', b'Ada'), (b'Agilent VEE', b'Agilent VEE'), (b'Algol', b'Algol'), (b'Alice', b'Alice'), (b'Angelscript', b'Angelscript'), (b'Apex', b'Apex'), (b'APL', b'APL'), (b'AppleScript', b'AppleScript'), (b'Arc', b'Arc'), (b'Arduino', b'Arduino'), (b'ASP', b'ASP'), (b'AspectJ', b'AspectJ'), (b'Assembly', b'Assembly'), (b'ATLAS', b'ATLAS'), (b'Augeas', b'Augeas'), (b'AutoHotkey', b'AutoHotkey'), (b'AutoIt', b'AutoIt'), (b'AutoLISP', b'AutoLISP'), (b'Automator', b'Automator'), (b'Avenue', b'Avenue'), (b'Awk', b'Awk'), (b'Bash', b'Bash'), (b'(Visual) Basic', b'(Visual) Basic'), (b'bc', b'bc'), (b'BCPL', b'BCPL'), (b'BETA', b'BETA'), (b'BlitzMax', b'BlitzMax'), (b'Boo', b'Boo'), (b'Bourne Shell', b'Bourne Shell'), (b'Bro', b'Bro'), (b'C', b'C'), (b'C Shell', b'C Shell'), (b'C#', b'C#'), (b'C++', b'C++'), (b'C++/CLI', b'C++/CLI'), (b'C-Omega', b'C-Omega'), (b'Caml', b'Caml'), (b'Ceylon', b'Ceylon'), (b'CFML', b'CFML'), (b'cg', b'cg'), (b'Ch', b'Ch'), (b'CHILL', b'CHILL'), (b'CIL', b'CIL'), (b'CL (OS/400)', b'CL (OS/400)'), (b'Clarion', b'Clarion'), (b'Clean', b'Clean'), (b'Clipper', b'Clipper'), (b'Clojure', b'Clojure'), (b'CLU', b'CLU'), (b'COBOL', b'COBOL'), (b'Cobra', b'Cobra'), (b'CoffeeScript', b'CoffeeScript'), (b'ColdFusion', b'ColdFusion'), (b'COMAL', b'COMAL'), (b'Common Lisp', b'Common Lisp'), (b'Coq', b'Coq'), (b'cT', b'cT'), (b'Curl', b'Curl'), (b'D', b'D'), (b'Dart', b'Dart'), (b'DCL', b'DCL'), (b'DCPU-16 ASM', b'DCPU-16 ASM'), (b'Delphi/Object Pascal', b'Delphi/Object Pascal'), (b'DiBOL', b'DiBOL'), (b'Dylan', b'Dylan'), (b'E', b'E'), (b'eC', b'eC'), (b'Ecl', b'Ecl'), (b'ECMAScript', b'ECMAScript'), (b'EGL', b'EGL'), (b'Eiffel', b'Eiffel'), (b'Elixir', b'Elixir'), (b'Emacs Lisp', b'Emacs Lisp'), (b'Erlang', b'Erlang'), (b'Etoys', b'Etoys'), (b'Euphoria', b'Euphoria'), (b'EXEC', b'EXEC'), (b'F#', b'F#'), (b'Factor', b'Factor'), (b'Falcon', b'Falcon'), (b'Fancy', b'Fancy'), (b'Fantom', b'Fantom'), (b'Felix', b'Felix'), (b'Forth', b'Forth'), (b'Fortran', b'Fortran'), (b'Fortress', b'Fortress'), (b'(Visual) FoxPro', b'(Visual) FoxPro'), (b'Gambas', b'Gambas'), (b'GNU Octave', b'GNU Octave'), (b'Go', b'Go'), (b'Google AppsScript', b'Google AppsScript'), (b'Gosu', b'Gosu'), (b'Groovy', b'Groovy'), (b'Haskell', b'Haskell'), (b'haXe', b'haXe'), (b'Heron', b'Heron'), (b'HPL', b'HPL'), (b'HyperTalk', b'HyperTalk'), (b'Icon', b'Icon'), (b'IDL', b'IDL'), (b'Inform', b'Inform'), (b'Informix-4GL', b'Informix-4GL'), (b'INTERCAL', b'INTERCAL'), (b'Io', b'Io'), (b'Ioke', b'Ioke'), (b'J', b'J'), (b'J#', b'J#'), (b'JADE', b'JADE'), (b'Java', b'Java'), (b'Java FX Script', b'Java FX Script'), (b'JavaScript', b'JavaScript'), (b'JScript', b'JScript'), (b'JScript.NET', b'JScript.NET'), (b'Julia', b'Julia'), (b'Korn Shell', b'Korn Shell'), (b'Kotlin', b'Kotlin'), (b'LabVIEW', b'LabVIEW'), (b'Ladder Logic', b'Ladder Logic'), (b'Lasso', b'Lasso'), (b'Limbo', b'Limbo'), (b'Lingo', b'Lingo'), (b'Lisp', b'Lisp'), (b'Logo', b'Logo'), (b'Logtalk', b'Logtalk'), (b'LotusScript', b'LotusScript'), (b'LPC', b'LPC'), (b'Lua', b'Lua'), (b'Lustre', b'Lustre'), (b'M4', b'M4'), (b'MAD', b'MAD'), (b'Magic', b'Magic'), (b'Magik', b'Magik'), (b'Malbolge', b'Malbolge'), (b'MANTIS', b'MANTIS'), (b'Maple', b'Maple'), (b'Mathematica', b'Mathematica'), (b'MATLAB', b'MATLAB'), (b'Max/MSP', b'Max/MSP'), (b'MAXScript', b'MAXScript'), (b'MEL', b'MEL'), (b'Mercury', b'Mercury'), (b'Mirah', b'Mirah'), (b'Miva', b'Miva'), (b'ML', b'ML'), (b'Monkey', b'Monkey'), (b'Modula-2', b'Modula-2'), (b'Modula-3', b'Modula-3'), (b'MOO', b'MOO'), (b'Moto', b'Moto'), (b'MS-DOS Batch', b'MS-DOS Batch'), (b'MUMPS', b'MUMPS'), (b'NATURAL', b'NATURAL'), (b'Nemerle', b'Nemerle'), (b'Nimrod', b'Nimrod'), (b'NQC', b'NQC'), (b'NSIS', b'NSIS'), (b'Nu', b'Nu'), (b'NXT-G', b'NXT-G'), (b'Oberon', b'Oberon'), (b'Object Rexx', b'Object Rexx'), (b'Objective-C', b'Objective-C'), (b'Objective-J', b'Objective-J'), (b'OCaml', b'OCaml'), (b'Occam', b'Occam'), (b'ooc', b'ooc'), (b'Opa', b'Opa'), (b'OpenCL', b'OpenCL'), (b'OpenEdge ABL', b'OpenEdge ABL'), (b'OPL', b'OPL'), (b'Oz', b'Oz'), (b'Paradox', b'Paradox'), (b'Parrot', b'Parrot'), (b'Pascal', b'Pascal'), (b'Perl', b'Perl'), (b'PHP', b'PHP'), (b'Pike', b'Pike'), (b'PILOT', b'PILOT'), (b'PL/I', b'PL/I'), (b'PL/SQL', b'PL/SQL'), (b'Pliant', b'Pliant'), (b'PostScript', b'PostScript'), (b'POV-Ray', b'POV-Ray'), (b'PowerBasic', b'PowerBasic'), (b'PowerScript', b'PowerScript'), (b'PowerShell', b'PowerShell'), (b'Processing', b'Processing'), (b'Prolog', b'Prolog'), (b'Puppet', b'Puppet'), (b'Pure Data', b'Pure Data'), (b'Python', b'Python'), (b'Q', b'Q'), (b'R', b'R'), (b'Racket', b'Racket'), (b'REALBasic', b'REALBasic'), (b'REBOL', b'REBOL'), (b'Revolution', b'Revolution'), (b'REXX', b'REXX'), (b'RPG (OS/400)', b'RPG (OS/400)'), (b'Ruby', b'Ruby'), (b'Rust', b'Rust'), (b'S', b'S'), (b'S-PLUS', b'S-PLUS'), (b'SAS', b'SAS'), (b'Sather', b'Sather'), (b'Scala', b'Scala'), (b'Scheme', b'Scheme'), (b'Scilab', b'Scilab'), (b'Scratch', b'Scratch'), (b'sed', b'sed'), (b'Seed7', b'Seed7'), (b'Self', b'Self'), (b'Shell', b'Shell'), (b'SIGNAL', b'SIGNAL'), (b'Simula', b'Simula'), (b'Simulink', b'Simulink'), (b'Slate', b'Slate'), (b'Smalltalk', b'Smalltalk'), (b'Smarty', b'Smarty'), (b'SPARK', b'SPARK'), (b'SPSS', b'SPSS'), (b'SQR', b'SQR'), (b'Squeak', b'Squeak'), (b'Squirrel', b'Squirrel'), (b'Standard ML', b'Standard ML'), (b'Suneido', b'Suneido'), (b'SuperCollider', b'SuperCollider'), (b'TACL', b'TACL'), (b'Tcl', b'Tcl'), (b'Tex', b'Tex'), (b'thinBasic', b'thinBasic'), (b'TOM', b'TOM'), (b'Transact-SQL', b'Transact-SQL'), (b'Turing', b'Turing'), (b'TypeScript', b'TypeScript'), (b'Vala/Genie', b'Vala/Genie'), (b'VBScript', b'VBScript'), (b'Verilog', b'Verilog'), (b'VHDL', b'VHDL'), (b'VimL', b'VimL'), (b'Visual Basic .NET', b'Visual Basic .NET'), (b'WebDNA', b'WebDNA'), (b'Whitespace', b'Whitespace'), (b'X10', b'X10'), (b'xBase', b'xBase'), (b'XBase++', b'XBase++'), (b'Xen', b'Xen'), (b'XPL', b'XPL'), (b'XSLT', b'XSLT'), (b'XQuery', b'XQuery'), (b'yacc', b'yacc'), (b'Yorick', b'Yorick'), (b'Z shell', b'Z shell')])),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
