import 'dart:io';

import 'package:flutter/material.dart';

import 'package:chaquopy/chaquopy.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:path_provider/path_provider.dart';

void main() {
  runApp(Emofun());
}

class Emofun extends StatefulWidget {
  @override
  EmofunState createState() => EmofunState();
}

class EmofunState extends State<Emofun> {
  String s='';
  String code='';
  String res='';
  bool flag=false;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner:false,
      home: Scaffold(
        backgroundColor: Colors.amberAccent,
        body: SingleChildScrollView(
          child: Column(
            children: [
              const SizedBox(
                height: 60,
              ),
              Center(
                child: Text('Emofun',style: GoogleFonts.cedarvilleCursive(color: Colors.black,fontSize: 32,fontWeight: FontWeight.w700),),
              ),
              const SizedBox(
                height: 10,
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Container(
                  width: double.infinity,
                  padding: EdgeInsets.all(20),
                  height: 500,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    color: Colors.white,
                  ),
                  child:!flag ? Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      const SizedBox(
                        height: 30,
                      ),
                      Text('Try Emofun!',style: GoogleFonts.poppins(fontSize: 28),),
                      const SizedBox(
                        height: 10,
                      ),
                      Container(
                        height: 200,
                        width: 350,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(20),
                          color: Colors.amberAccent.withOpacity(0.3),
                        ),
                        child: Center(
                          child: TextField(
                            style: GoogleFonts.poppins(fontSize: 16),
                            decoration: const InputDecoration(
                              border: InputBorder.none,
                              hintText: 'Type Here ...'
                            ),
                            minLines: 2,
                            maxLines: 5,
                            cursorColor: Colors.amber,
                            onChanged: (String value)
                            {
                              s=value;
                            },
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 60,
                      ),
                      GestureDetector(
                        onTap: () async{
                          code='''
import emoji
import random
from os.path import dirname, join
options = [ emoji.UNICODE_EMOJI_ENGLISH, emoji.UNICODE_EMOJI_ALIAS_ENGLISH,
            emoji.UNICODE_EMOJI_ITALIAN,emoji.UNICODE_EMOJI_SPANISH,
            emoji.UNICODE_EMOJI_PORTUGUESE  ]
choi = random.choice(options)
emo = []
for i in choi:
    emo.append(i)
f="${s}"
words = f.split(' ')

ans = ''
for w in words:
    # print(w,' ',random.choice(emo))
    ans += w + ' ' + random.choice(emo)
print(ans)

''';
                          final _result =
                          await Chaquopy.executeCode(code);
                          setState(() {
                            res = _result['textOutputOrError'] ?? '';
                            flag=true;
                          });
                        },
                        child: Container(
                          height: 70,
                          width: 350,
                           color: Colors.amber,
                           child: Center(child: Text('Convert',style: GoogleFonts.poppins(fontSize: 24),)),
                          ),
                      ),
                    ],
                  ):Column(
                    children: [
                      const SizedBox(
                        height: 40,
                      ),
                      Text('Your Result',style: GoogleFonts.poppins(fontSize: 28),),
                      const SizedBox(height: 30,),
                      GestureDetector(
                        onTap: (){
                          Clipboard.setData( ClipboardData(text: res));
                        },
                        child: Container(
                          height: 250,
                          color: Colors.amberAccent.withOpacity(0.3),
                          child: Center(
                            child: Text(res,style: GoogleFonts.poppins(fontSize: 16),),
                          ),
                        ),
                      ),
                      const SizedBox(height: 20,),
                      GestureDetector(
                        onTap: (){
                          flag=false;
                          setState(() {

                          });
                        },
                        child: Container(
                          height: 70,
                          width: 350,
                          color: Colors.amber,
                          child: Center(child: Text('Try Again',style: GoogleFonts.poppins(fontSize: 24),)),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
