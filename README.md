# MakeItSquare.py

MakeItSquare.py is a script for destroying an audio file of your choice. By amplifying differences between samples of the audio file, the script produces a "deep fry" effect useful for instrumental effects or just simple fun.

Where MakeItSquare.py differs from traditional amplify-with-clip approaches is in its amplification approach. Rather than indiscriminately setting samples above the x axis to their maximum value and those below the axis to their minimum, MakeItSquare.py uses the difference between two samples to select the appropriate extreme. When no threshold is applied, this has the effect of maximizing the power of all frequencies in the signal equally without eliminating treble. Perceptually speaking, this results in a thinner, white noise-like result that strongly favors percussion and other high-frequency signals.

## Usage

`MakeItSquare.py filename outname threshold`

### Parameters

- `filename` (*str*): The complete absolute path of the file to be read.
- `outname` (*str*, optional): The complete absolute path of the file to be output. Defaults to `"./out.wav"`.
- `threshold` (*float*, optional): The minimum change in position of the signal (as a proportion of its total range, out of 2.0) for a new jump to occur. For example, if `threshold` is set to `0.1`, only a change in the signal greater than 5% of its maximum total range will be amplified. Consequently, this cuts off portions of the signal which do not meet a minimum power requirement to be amplified and has the effect of reducing sibilance proportionately to the value. Defaults to `0.0`.