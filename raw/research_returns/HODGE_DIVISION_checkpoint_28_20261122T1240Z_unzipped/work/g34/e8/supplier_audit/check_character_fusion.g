Read("common_actual.g");
Read("actual_setup_data.g");
t0:=Runtime();;
ta:=CharacterTable(GW);;
ca:=ConjugacyClasses(ta);;
Print("Fresh actual table classes ",Length(ca)," ms ",Runtime()-t0,"\n");
fusion:=List(ca,c->GKey(Representative(c))[2]);;
Assert(0,Set(fusion)=[1..NC]);
ia:=Irr(ta);;
Print("Fresh actual irreducibles ",Length(ia)," ms ",Runtime()-t0,"\n");
transported:=List(irr,ch->ch{fusion});;
Assert(0,Set(List(ia,ValuesOfClassFunction))=Set(transported));
irrfusion:=List(irr,ch->Position(List(ia,ValuesOfClassFunction),ch{fusion}));;
PrintTo("character_fusion_result.g","FUSION := ",fusion,";\n",
  "IRRFUSION := ",irrfusion,";\n",
  "ACTUAL_IRREDUCIBLES := ",List(ia,ValuesOfClassFunction),";\n");
Print("FULL actual irreducible/library class identification PASS\n");
QUIT;
