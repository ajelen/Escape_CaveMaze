# -*- coding: UTF-8 -*-
print "Pozdravljeni v jamskem blodnjaku!"
print "Tvoja naloga je varno prečkati blodnjak in najti njegovo središče."

print "Podaj se po blodnjaku naravnost, kmalu boš prišel do prvega križišča ..."
print "... kjer pa se boš moral odločiti, skozi kateri vhod boš šel - 1, 2 ali 3?"

vhod = raw_input("> ")

if vhod == "1":
	print """Prišel si do brezna. Ob robu je majhna polica. 
	Lahko bi šel po njej, a je to lahko zelo nevarno."""
	print """Za njegovo prečenje imaš na voljo tri predmete. 
	Izbiraš lahko med 1 - deska, 2 - vrv z osebno opremo, 3 - metla s čelado."""
	predmet = raw_input("> ")

	if predmet == "1":
		print """Deska je kar dobra izbira, a je prekratka. Če imaš prijatelja s sabo, 
		si nekako pomagajta in s pomočjo deske preskočita brezno."""
		print "Saj zmoreš, uspelo ti bo!"
	elif predmet == "2":
		print """Očitno ti jamarstvo ni tako tuje in veš, da je prečenje 
		brezna po prečki res najvarnejše. Super!"""
	elif predmet == "3":
		print "Hja, metle so za coprnice, tebi pa v tej situaciji ne bo ravno pomagala."
		print "Poskusi v steni najti skrivni izhod, saj zaupaš v svoje zmožnosti!"
	else:
		print """Tega predmeta pa žal nimamo, morda damo na seznam želja! 
		Saj bo, ne obupaj že na začetku."""

elif vhod == "2":
	print "Nahajaš se v podorni dvorani. Vse okoli tebe so veliki podorni bloki."
	print """Tvoja naloga je, da se varno splaziš skozi ožino. 
	Pred tabo sta dva bloka. 
	Izberi pod katerega boš šel: 1 ali 2?"""
	podorni_blok = raw_input("> ")

	if podorni_blok == "1":
		print "Ups skala se je premaknila! Ostal si ujet v grajski ječi."
		print "Počakaj, da ti kazen mine. Čas si krajšaj z ogledom skrivnostnih zgodb."
	elif podorni_blok == "2":
		print """Na pomoč ti je prišla princesa Veronika. Odpeljala te je v majhno sobico, 
		kjer ji moraš pomagati pri izdelovanju pletene košare iz vozlov."""
		print """Za nalogo si dobil izdelavo osmic in šestic. Veronika bo odločila, 
		če si zadevo dobro opravil in nadaljuješ pot - 1, 
		ali te bo zaprla v grajsko ječo - 2."""
		Veronikina_naloga = raw_input("> ")

		if Veronikina_naloga == "1":
			print "Dobro si opravil. Zaslužil si si pravo gostijo!"
		elif Veronikina_naloga == "2":
			print """Veronika ni bila zadovoljna s košaro. 
			Postal si jetnik! Počakaj, da mine kazen. Na stenah so skrivnostni obrazi.    
			Dotakni se katerega izmed njih in poslušaj njegovo zgodbo.""" 					#Kot pri Game of Thrones.
						
	else:
		print "Slabo ti gre štetje, samo dva bloka sta!"

elif vhod == "3":
	print """Kakšna smola, pred tabo se je odprl rov, ki nima nadaljevanja!
	Ampak vse ni tako črnogledo. Pred tabo se skrivata dva načina, kako prečkati ta slepi rov!
	Za prvi namig pritisni 1, za drugi pa 2!"""
	slepi_rov = raw_input("> ")

	if slepi_rov == "1":
		print "Na koncu rova je kotanja z vodo. Podrobno jo poglej in se splazi skozi sifon."
		print "Prišel si skozi, sedaj pa se splazi po trebuhu do naslednjega križišča."
		print """V ospredju vidiš dva rova. V prvem (1) nekaj močno šumi in buči. V drugem (2) pa je vse mirno in tiho.
		Z vpisom številke se odloči, kam te bo vodila pot naprej."""
		dva_rova = raw_input("> ")

		if dva_rova == "1":
			print """Zelo si pogumen! Ni te strah sprejeti odločitev. Šum in bučenje v ospredju je bilo pretakajoče jezero.
			Zelo lep prizor. Vzemi čoln in se odpelji nasproti toka vode."""
			print """Prišel si do majhne sobice, kjer vidiš odsev dekleta, ki si poje pesem.
			Če te njeno petje ne zanima in ti ni všeč, pritisni 1 in pojdi naprej. Če pa ti je všeč, pritisni 2."""
			petje_dekleta = raw_input("> ")

			if petje_dekleta == "1":
				print "Jamski zvoki ti niso všeč. Rad ti čimprej prišel iz te luknje."
				print "Pojdi v naslednjo sobo, kjer pa ti zmanjka baterije in moraš najti pravi izhod."
				print "Izbral si 1 - izhod, 2 - izhod, 3 -izhod."
			elif petje_dekleta == "2":
				print "Bobni ti delujejo mistično. Usedi se bližje, saj tu je izvir termalne vode! Uživaj v glasbi!"
				print "Ko se glasba konča, je čas, da nadaljuješ svojo pot."
				print "Izberi ustrezni izhod: 1, 2 ali 3?"
				izhod = raw_input("> ")

				if izhod == "1":
					print """Ne oklevaš pri izbiri in takoj izbereš prvo, kar je. 
					Ta odločitev te je pripeljala do spusta po blatni drči.
					Si že zelo blizu središča blodnjaka. Samo še malo."""
				elif izhod == "2":
					print """Ne mudi se ti še končati avanturo, zato si se udeležil
					tečaja izdelovanja mističnih figuric iz gline. Ob tem se sprošča
					endorfini - hormoni sreče, zato si le vzemi čas in izdelaj kaj 
					lepega!"""
				elif izhod == "3":
					print "Prišel si do središča blodnjaka!"

else:
	print "Moraš se odločiti, skozi kateri vhod boš prišel do središča blodnjaka."


