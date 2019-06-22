#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include<Fl/Fl_Widget.H>
#include <FL/Fl_Int_Input.H>
#include<string>
#include<unistd.h>
#include<iostream>
#include <ctime>
#include<cstdlib>
#include <FL/Fl_Box.H>

void newTextValue(Fl_Widget *w, void *p);





int main(int argc, char **argv)
{
    Fl_Window *window = new Fl_Window(340,180);
    //Fl_Widget *w1 = new Fl_Widget(100,20,100,100,"CPPHyperloop");
    Fl_Int_Input *text = new Fl_Int_Input(100,100,100,100,"CPPHyperloop");
    srand (time(NULL));
    int r = rand() % 10;
    
    const char *words [3];
    words[0] = "hi";
    words[1] = "bye";
    words[2] = "sup";

    
  
    text->value(23);
    text->when(FL_WHEN_RELEASE_ALWAYS);
    
    text->callback(newTextValue,&r);
    
    text->when(FL_WHEN_CHANGED);  
    
    
    
    

     

    window->end();
    window->show(argc, argv);
    return Fl::run();
}

void newTextValue(Fl_Widget* w, void* p)
{
    
    Fl_Int_Input* I =(Fl_Int_Input*)w;
   
    
        I->value((const char*)p);
        I->resize(100,100,100,100);
        Fl::check();
        I->redraw();   
    
      
    
  
   


}    
    

    


    
