import wx
from backend1 import bmi_calculator, symptom_checker, age_group_analyzer, generate_token_for

def on_bmi(event):
    weight = wx.GetTextFromUser("Enter weight (kg):", "BMI Calculator")
    height = wx.GetTextFromUser("Enter height (cm):", "BMI Calculator")
    if weight and height:
        bmi, category = bmi_calculator(float(weight), float(height))

        # --- Custom BMI Output Frame ---
        output = wx.Frame(None, title="BMI Result", size=(400, 180))
        panel = wx.Panel(output)

        # Display BMI text
        wx.StaticText(panel, label=f"Your BMI is {bmi:.2f} ({category})", pos=(20, 10))

        # Draw gradient scale and pointer
        def draw_scale(event):
            dc = wx.PaintDC(panel)
            w, h = panel.GetSize()
            x_start, y_start = 20, 50
            scale_width, scale_height = 340, 30

            # Draw gradient
            for i in range(scale_width):
                ratio = i / scale_width
                # Interpolating from blue -> green -> yellow -> red
                if ratio < 0.462:  # up to 18.5/40
                    r = int(173 + (0-173)*(ratio/0.462))
                    g = int(216 + (255-216)*(ratio/0.462))
                    b = int(230 + (0-230)*(ratio/0.462))
                elif ratio < 0.623:  # 18.5 to 24.9
                    r = int(0 + (255-0)*((ratio-0.462)/0.161))
                    g = int(255 + (255-255)*((ratio-0.462)/0.161))
                    b = int(0 + (0-0)*((ratio-0.462)/0.161))
                elif ratio < 0.748:  # 25 to 29.9
                    r = 255
                    g = int(255 - 255*((ratio-0.623)/0.125))
                    b = 0
                else:  # 30 to 40
                    r = 255
                    g = 0
                    b = 0
                dc.SetPen(wx.Pen(wx.Colour(r, g, b)))
                dc.DrawLine(x_start+i, y_start, x_start+i, y_start+scale_height)

            # Draw BMI pointer
            bmi_pos = x_start + int((bmi / 40) * scale_width)
            dc.SetBrush(wx.Brush("white"))
            dc.DrawPolygon([ (bmi_pos-5, y_start-5),
                             (bmi_pos+5, y_start-5),
                             (bmi_pos, y_start+scale_height+5) ])

            # Optional labels
            # Optional labels with adjusted y positions
            dc.DrawText("Underweight", x_start, y_start + scale_height + 10)
            dc.DrawText("Normal", x_start + int(scale_width*0.462), y_start + scale_height + 10)
            dc.DrawText("Overweight", x_start + int(scale_width*0.623), y_start + scale_height + 10) 
            dc.DrawText("Obese", x_start + int(scale_width*0.9), y_start + scale_height + 10)       


        panel.Bind(wx.EVT_PAINT, draw_scale)
        output.Show()


def on_symptom(event):
    symptoms = wx.GetTextFromUser("Enter symptoms (comma separated):", "Symptom Checker")
    if symptoms:
        results = symptom_checker(symptoms.split(","))
        wx.MessageBox("\n".join(results), "Results")

def on_age(event):
    ages = wx.GetTextFromUser("Enter ages (comma separated):", "Age Group Analyzer")
    if ages:
        age_list = [int(a.strip()) for a in ages.split(",")]
        distribution = age_group_analyzer(age_list)
        msg = "\n".join([f"{group}: {count}" for group, count in distribution.items()])
        wx.MessageBox(msg, "Age Distribution")

def on_token(event):
    name = wx.GetTextFromUser("Enter patient name:", "Appointment Token Generator")
    if name:
        token = generate_token_for(name)
        wx.MessageBox(f"Appointment token for {name} generated: {token}", "Token Generated")
        


app = wx.App()

frame = wx.Frame(None, title="Healthcare Utility System", size=(350, 300))
panel = wx.Panel(frame)
panel.SetBackgroundColour("light blue")
vbox = wx.BoxSizer(wx.VERTICAL)

btn_bmi = wx.Button(panel, label="BMI Calculator")
btn_symptom = wx.Button(panel, label="Symptom Checker")
btn_age = wx.Button(panel, label="Age Group Analyzer")
btn_token = wx.Button(panel, label="Appointment Token Generator")

btn_bmi.Bind(wx.EVT_BUTTON, on_bmi)
btn_symptom.Bind(wx.EVT_BUTTON, on_symptom)
btn_age.Bind(wx.EVT_BUTTON, on_age)
btn_token.Bind(wx.EVT_BUTTON, on_token)

for btn in [btn_bmi, btn_symptom, btn_age, btn_token]:
    vbox.Add(btn, 0, wx.EXPAND | wx.ALL, 10)

panel.SetSizer(vbox)
frame.Show()
app.MainLoop()




