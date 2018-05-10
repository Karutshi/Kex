prestr = """<?xml version="1.0" encoding="utf-8"?>
<ExperimentSettings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <MergeConsecutiveFixations>true</MergeConsecutiveFixations>
  <EliminateFirstFixation>false</EliminateFirstFixation>
  <LimitForFirstFixation>300</LimitForFirstFixation>
  <EliminateFirstFixationSimple>false</EliminateFirstFixationSimple>
  <SerializableVersion>5.0.5754.30197</SerializableVersion>
  <GazeSamplingRate>60</GazeSamplingRate>
  <GazeMaxDistance>20</GazeMaxDistance>
  <GazeMinSamples>5</GazeMinSamples>
  <GazeDiameterDiv>2</GazeDiameterDiv>
  <MouseSamplingRate>10</MouseSamplingRate>
  <MouseMaxDistance>20</MouseMaxDistance>
  <MouseMinSamples>10</MouseMinSamples>
  <MouseDiameterDiv>5</MouseDiameterDiv>
  <FixationRingSize>31</FixationRingSize>
  <WidthStimulusScreen>1920</WidthStimulusScreen>
  <HeightStimulusScreen>1080</HeightStimulusScreen>
  <Name>kex</Name>
  <SqlInstanceName>SQLEXPRESS</SqlInstanceName>
  <CustomConnectionString />
  <SlideShow>
    <IsModified>false</IsModified>
    <CustomShuffling>
      <UseThisCustomShuffling>false</UseThisCustomShuffling>
      <ShuffleSectionsParentNodeID>1</ShuffleSectionsParentNodeID>
      <ShuffleSectionItems>true</ShuffleSectionItems>
      <NumItemsOfSectionInGroup>1</NumItemsOfSectionInGroup>
      <ShuffleGroups>true</ShuffleGroups>
      <ShuffleGroupItems>false</ShuffleGroupItems>
    </CustomShuffling>
	<SlideshowTreeNode>
      <Name>70</Name>
      <Randomize>false</Randomize>
      <NumberOfItemsToUse>0</NumberOfItemsToUse>
      <Slide>
        <IsDisabled>false</IsDisabled>
        <IdOfPreSlideFixationTrial>-1</IdOfPreSlideFixationTrial>
        <PresentationSize>
          <Width>1920</Width>
          <Height>1080</Height>
        </PresentationSize>
        <Modified>true</Modified>
        <IsDesktopSlide>false</IsDesktopSlide>
        <VGStimuli>
          <VGElement xsi:type="VGText">
            <Name />
            <StyleGroup>AOI_NORMAL</StyleGroup>
            <ElementGroup />
            <SerializedPen>Color: FFFF0000;1 px;Solid;StartCap :Flat;EndCap :Flat;CustomStartCap AdjustableArrow:;CustomEndCap AdjustableArrow:</SerializedPen>
            <SerializedBrush>SolidBrush;FFFF0000</SerializedBrush>
            <SerializedFont>Microsoft Sans Serif, 8.25pt</SerializedFont>
            <SerializedFontColor>FF6D6D6D</SerializedFontColor>
            <ShapeDrawAction>None</ShapeDrawAction>
            <Size>
              <Width>859.896362</Width>
              <Height>46</Height>
            </Size>
            <Location>
              <X>470.051819</X>
              <Y>513</Y>
            </Location>
            <Visible>true</Visible>
            <SerializableModifierKeys>None</SerializableModifierKeys>
            <Sound>
              <Filename />
              <ShouldPlay>false</ShouldPlay>
              <Loop>false</Loop>
              <ShowOnClick>false</ShowOnClick>
            </Sound>
            <TextAlignment>Center</TextAlignment>
            <OnsetTime>0</OnsetTime>
            <EndTime>0</EndTime>
            <StringToDraw>Press the screen when you are ready to begin.</StringToDraw>
            <Alignment>Left</Alignment>
            <SerializedTextFont>Arial, 24pt</SerializedTextFont>
            <SerializedTextFontColor>FF00B9EE</SerializedTextFontColor>
          </VGElement>
        </VGStimuli>
        <ActiveXStimuli />
        <Name>FirstSlide</Name>
        <Category />
        <StopConditions>
          <StopCondition xsi:type="MouseStopCondition">
            <IsCorrectResponse xsi:nil="true" />
            <CanBeAnyInputOfThisType>false</CanBeAnyInputOfThisType>
            <TrialID xsi:nil="true" />
            <StopMouseButton>Left</StopMouseButton>
            <ClickLocation>
              <X>0</X>
              <Y>0</Y>
            </ClickLocation>
            <Target />
          </StopCondition>
        </StopConditions>
        <SerializedBackgroundColor>FF000000</SerializedBackgroundColor>
        <BackgroundSound>
          <Filename />
          <ShouldPlay>false</ShouldPlay>
          <Loop>false</Loop>
          <ShowOnClick>false</ShowOnClick>
        </BackgroundSound>
        <TriggerSignal>
          <Signaling>None</Signaling>
          <OutputDevice>LPT</OutputDevice>
          <Value>255</Value>
          <SignalingTime>10</SignalingTime>
          <PortAddress>888</PortAddress>
        </TriggerSignal>
        <CorrectResponses />
        <Links />
        <TargetShapes />
        <MouseCursorVisible>true</MouseCursorVisible>
        <MouseInitialPosition>
          <X>960</X>
          <Y>540</Y>
        </MouseInitialPosition>
        <ForceMousePositionChange>true</ForceMousePositionChange>
      </Slide>
      <Tag />
      <Text>FirstSlide</Text>
    </SlideshowTreeNode>
"""
poststr = """  </SlideShow>
  <GazeColorParams>
    <SubjectStyles />
    <CategoryStyles />
    <ColorizationMode>Gradient</ColorizationMode>
  </GazeColorParams>
  <MouseColorParams>
    <SubjectStyles />
    <CategoryStyles />
    <ColorizationMode>Gradient</ColorizationMode>
  </MouseColorParams>
  <ScreenCaptureFramerate>10</ScreenCaptureFramerate>
</ExperimentSettings>
""" 
longstr = """
      <SlideshowTreeNode>
        <Name>{name2}</Name>
        <Randomize>false</Randomize>
        <NumberOfItemsToUse>0</NumberOfItemsToUse>
        <Slide>
          <IsDisabled>false</IsDisabled>
          <IdOfPreSlideFixationTrial>-1</IdOfPreSlideFixationTrial>
          <PresentationSize>
            <Width>1920</Width>
            <Height>1080</Height>
          </PresentationSize>
          <Modified>true</Modified>
          <IsDesktopSlide>false</IsDesktopSlide>
          <VGStimuli />
          <ActiveXStimuli>
            <VGElement xsi:type="VGFlash">
              <Name />
              <StyleGroup>ACTIVEX</StyleGroup>
              <ElementGroup />
              <SerializedPen>Color: FFFF0000;1 px;Solid;StartCap :Flat;EndCap :Flat;CustomStartCap AdjustableArrow:;CustomEndCap AdjustableArrow:</SerializedPen>
              <SerializedBrush>SolidBrush;FFFF0000</SerializedBrush>
              <SerializedFont>Microsoft Sans Serif, 8.25pt</SerializedFont>
              <SerializedFontColor>FF6D6D6D</SerializedFontColor>
              <ShapeDrawAction>None</ShapeDrawAction>
              <Size>
                <Width>1920</Width>
                <Height>1080</Height>
              </Size>
              <Location>
                <X>0</X>
                <Y>0</Y>
              </Location>
              <Visible>true</Visible>
              <SerializableModifierKeys>None</SerializableModifierKeys>
              <Sound>
                <Filename />
                <ShouldPlay>false</ShouldPlay>
                <Loop>false</Loop>
                <ShowOnClick>false</ShowOnClick>
              </Sound>
              <TextAlignment>Center</TextAlignment>
              <OnsetTime>0</OnsetTime>
              <EndTime>0</EndTime>
              <Filename>{videonumber}.swf</Filename>
              <Bounds>
                <Location>
                  <X>0</X>
                  <Y>0</Y>
                </Location>
                <Size>
                  <Width>1920</Width>
                  <Height>1080</Height>
                </Size>
                <X>0</X>
                <Y>0</Y>
                <Width>1920</Width>
                <Height>1080</Height>
              </Bounds>
            </VGElement>
          </ActiveXStimuli>
          <Name>S{videonumber}</Name>
          <Category />
          <StopConditions>
            <StopCondition xsi:type="TimeStopCondition">
              <IsCorrectResponse xsi:nil="true" />
              <Duration>20000</Duration>
            </StopCondition>
          </StopConditions>
          <SerializedBackgroundColor>FF000000</SerializedBackgroundColor>
          <BackgroundSound>
            <Filename />
            <ShouldPlay>false</ShouldPlay>
            <Loop>false</Loop>
            <ShowOnClick>false</ShowOnClick>
          </BackgroundSound>
          <TriggerSignal>
            <Signaling>None</Signaling>
            <OutputDevice>LPT</OutputDevice>
            <Value>255</Value>
            <SignalingTime>10</SignalingTime>
            <PortAddress>888</PortAddress>
          </TriggerSignal>
          <CorrectResponses />
          <Links />
          <TargetShapes />
          <MouseCursorVisible>true</MouseCursorVisible>
          <MouseInitialPosition>
            <X>960</X>
            <Y>540</Y>
          </MouseInitialPosition>
          <ForceMousePositionChange>true</ForceMousePositionChange>
        </Slide>
        <Tag />
        <Text>{text2}</Text>
      </SlideshowTreeNode>
	  <SlideshowTreeNode>
        <Name>{name1}</Name>
        <Randomize>false</Randomize>
        <NumberOfItemsToUse>0</NumberOfItemsToUse>
        <Slide>
          <IsDisabled>false</IsDisabled>
          <IdOfPreSlideFixationTrial>-1</IdOfPreSlideFixationTrial>
          <PresentationSize>
            <Width>1920</Width>
            <Height>1080</Height>
          </PresentationSize>
          <Modified>true</Modified>
          <IsDesktopSlide>false</IsDesktopSlide>
          <VGStimuli>
            <VGElement xsi:type="VGText">
              <Name />
              <StyleGroup>AOI_NORMAL</StyleGroup>
              <ElementGroup />
              <SerializedPen>Color: FFFF0000;1 px;Solid;StartCap :Flat;EndCap :Flat;CustomStartCap AdjustableArrow:;CustomEndCap AdjustableArrow:</SerializedPen>
              <SerializedBrush>SolidBrush;FFFF0000</SerializedBrush>
              <SerializedFont>Microsoft Sans Serif, 8.25pt</SerializedFont>
              <SerializedFontColor>FF6D6D6D</SerializedFontColor>
              <ShapeDrawAction>None</ShapeDrawAction>
              <Size>
                <Width>743.9066</Width>
                <Height>138</Height>
              </Size>
              <Location>
                <X>358.953369</X>
                <Y>455.673584</Y>
              </Location>
              <Visible>true</Visible>
              <SerializableModifierKeys>None</SerializableModifierKeys>
              <Sound>
                <Filename />
                <ShouldPlay>false</ShouldPlay>
                <Loop>false</Loop>
                <ShowOnClick>false</ShowOnClick>
              </Sound>
              <TextAlignment>Center</TextAlignment>
              <OnsetTime>0</OnsetTime>
              <EndTime>0</EndTime>
              <StringToDraw>Previous video had ID: 
Please fill in your answers on the form, and then press the screen to continue.</StringToDraw>
              <Alignment>Left</Alignment>
              <SerializedTextFont>Arial, 24pt</SerializedTextFont>
              <SerializedTextFontColor>FFB4B4EC</SerializedTextFontColor>
            </VGElement>
            <VGElement xsi:type="VGText">
              <Name />
              <StyleGroup>AOI_NORMAL</StyleGroup>
              <ElementGroup />
              <SerializedPen>Color: FFFF0000;1 px;Solid;StartCap :Flat;EndCap :Flat;CustomStartCap AdjustableArrow:;CustomEndCap AdjustableArrow:</SerializedPen>
              <SerializedBrush>SolidBrush;FFFF0000</SerializedBrush>
              <SerializedFont>Microsoft Sans Serif, 8.25pt</SerializedFont>
              <SerializedFontColor>FF6D6D6D</SerializedFontColor>
              <ShapeDrawAction>None</ShapeDrawAction>
              <Size>
                <Width>253.678711</Width>
                <Height>62</Height>
              </Size>
              <Location>
                <X>758.4715</X>
                <Y>445.383362</Y>
              </Location>
              <Visible>true</Visible>
              <SerializableModifierKeys>None</SerializableModifierKeys>
              <Sound>
                <Filename />
                <ShouldPlay>false</ShouldPlay>
                <Loop>false</Loop>
                <ShowOnClick>false</ShowOnClick>
              </Sound>
              <TextAlignment>Center</TextAlignment>
              <OnsetTime>0</OnsetTime>
              <EndTime>0</EndTime>
              <StringToDraw>{sid}</StringToDraw>
              <Alignment>Left</Alignment>
              <SerializedTextFont>Arial, 32pt</SerializedTextFont>
              <SerializedTextFontColor>FFFF180C</SerializedTextFontColor>
            </VGElement>
          </VGStimuli>
          <ActiveXStimuli />
          <Name>Slide49</Name>
          <Category />
          <StopConditions>
            <StopCondition xsi:type="MouseStopCondition">
              <IsCorrectResponse xsi:nil="true" />
              <CanBeAnyInputOfThisType>false</CanBeAnyInputOfThisType>
              <TrialID xsi:nil="true" />
              <StopMouseButton>Left</StopMouseButton>
              <ClickLocation>
                <X>0</X>
                <Y>0</Y>
              </ClickLocation>
              <Target />
            </StopCondition>
          </StopConditions>
          <SerializedBackgroundColor>FF000000</SerializedBackgroundColor>
          <BackgroundSound>
            <Filename />
            <ShouldPlay>false</ShouldPlay>
            <Loop>false</Loop>
            <ShowOnClick>false</ShowOnClick>
          </BackgroundSound>
          <TriggerSignal>
            <Signaling>None</Signaling>
            <OutputDevice>LPT</OutputDevice>
            <Value>255</Value>
            <SignalingTime>10</SignalingTime>
            <PortAddress>888</PortAddress>
          </TriggerSignal>
          <CorrectResponses />
          <Links />
          <TargetShapes />
          <MouseCursorVisible>true</MouseCursorVisible>
          <MouseInitialPosition>
            <X>960</X>
            <Y>540</Y>
          </MouseInitialPosition>
          <ForceMousePositionChange>true</ForceMousePositionChange>
        </Slide>
        <Tag />
        <Text>{text1}</Text>
      </SlideshowTreeNode>

"""
groupstr = """     
    <SlideshowTreeNode>
      <Name>{num}</Name>
      <Randomize>false</Randomize>
      <NumberOfItemsToUse>0</NumberOfItemsToUse>
      <Tag />
      <Text>Group {grpnum}</Text>
    """

def getOrder(offset):
    latinsquare = [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    return [(i + offset - 1) % 12 for i in latinsquare]
	
def getGroupOrder(subject_number):
    return [(i + subject_number - 1) % 4 for i in [0, 3, 1, 2]]
	
l = [
     # Group 1
     [('sparse_11', 1),  ('sparse_32', 11), ('sparse_22_1', 5), ('sparse_00_1', 13), ('sparse_00_5', 33), ('sparse_00_9', 37),  
      ('dense_11', 17),  ('dense_32', 27), ('dense_22_1', 21), ('dense_00_1', 29), ('dense_00_5', 41), ('dense_00_9', 45)],
     # Group 2
     [('sparse_31', 10), ('sparse_12', 2),  ('sparse_22_2', 6), ('sparse_00_2', 14), ('sparse_00_6', 34), ('sparse_00_10', 38),
      ('dense_31', 26), ('dense_12', 18),  ('dense_22_2', 22), ('dense_00_2', 30), ('dense_00_6', 42), ('dense_00_10', 46)],
     # Group 3
     [('sparse_13', 3),  ('sparse_21', 4),  ('sparse_22_3', 7), ('sparse_00_3', 15), ('sparse_00_7', 35), ('sparse_00_11', 39),
      ('dense_13', 19),  ('dense_21', 20),  ('dense_22_3', 23), ('dense_00_3', 31), ('dense_00_7', 43), ('dense_00_11', 47)],
     # Group 4
     [('sparse_33', 12), ('sparse_23', 9),  ('sparse_22_4', 8), ('sparse_00_4', 16), ('sparse_00_8', 36), ('sparse_00_12', 40),
      ('dense_33', 28), ('dense_23', 25),  ('dense_22_4', 24), ('dense_00_4', 32), ('dense_00_8', 44), ('dense_00_12', 48)]
    ]

subject_number = input("Enter the subject number: ")

def write_video(f, v_name, v_id, i):
    f.write(longstr.format(name1 = i + 48, sid = v_id, text1 = str(v_id) + "_label", name2 = i, videonumber = v_name, text2 = str(v_id)))

with open('Kex.oga', 'w') as f:
    f.write(prestr)
    for grpnum in getGroupOrder(subject_number):
        videos = l[grpnum]
        f.write(groupstr.format(num = str(grpnum), grpnum = str(grpnum)))
        print("Group %d:" % grpnum)
        for i in getOrder(subject_number + grpnum * 3):
            v_name, v_id = videos[i]
            print("    Video %s with id %d" % (v_name, v_id))
            write_video(f, v_name, v_id, grpnum * 12 + 5 + i)
        f.write("    </SlideshowTreeNode>\n")
    f.write(poststr)
    print("Ogama settings file created as 'Kex.oga'")
