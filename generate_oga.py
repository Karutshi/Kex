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
              <SerializedFontColor>FF0000</SerializedFontColor>
              <ShapeDrawAction>None</ShapeDrawAction>
              <Size>
                <Width>1200</Width>
                <Height>138</Height>
              </Size>
              <Location>
                <X>170</X>
                <Y>450</Y>
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
              <StringToDraw>Id: {sid}
Please write down the required information on your sheet,
and then press the screen to view the video.</StringToDraw>
              <Alignment>Left</Alignment>
              <SerializedTextFont>Arial, 24pt</SerializedTextFont>
              <SerializedTextFontColor>FF2E2EBF</SerializedTextFontColor>
            </VGElement>
          </VGStimuli>
          <ActiveXStimuli />
          <Name>Slide0</Name>
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

"""
shortstr = """     
    <SlideshowTreeNode>
      <Name>{num}</Name>
      <Randomize>false</Randomize>
      <NumberOfItemsToUse>0</NumberOfItemsToUse>
      <Tag />
      <Text>Group {grpnum}</Text>
    """

l = [
     # Group 1
     [('sparse_11', 1),  ('sparse_32', 11), ('sparse_22_1', 5), ('sparse_00_1', 13), ('sparse_00_5', 33), ('sparse_00_9', 37),  
      ('dense_11', 17),  ('dense_32', 27), ('dense_22_1', 21), ('dense_00_1', 29), ('dense_00_5', 41), ('dense_00_9', 45)],
     # Group 2
     [('sparse_31', 10), ('sparse_12', 2),  ('sparse_22_2', 6), ('sparse_00_2', 14), ('sparse_00_6', 34), ('sparse_00_10', 38),
      ('dense_31', 10), ('dense_12', 2),  ('dense_22_2', 6), ('dense_00_2', 14), ('dense_00_6', 42), ('dense_00_10', 46)],
     # Group 3
     [('sparse_13', 3),  ('sparse_21', 4),  ('sparse_22_3', 7), ('sparse_00_3', 15), ('sparse_00_7', 35), ('sparse_00_11', 39),
      ('dense_13', 3),  ('dense_21', 4),  ('dense_22_3', 7), ('dense_00_3', 15), ('dense_00_7', 43), ('dense_00_11', 47)],
     # Group 4
     [('sparse_33', 12), ('sparse_23', 9),  ('sparse_22_4', 8), ('sparse_00_4', 16), ('sparse_00_8', 36), ('sparse_00_12', 40),
      ('dense_33', 12), ('dense_23', 9),  ('dense_22_4', 8), ('dense_00_4', 16), ('dense_00_8', 44), ('dense_00_12', 48)]
    ]


def badognasty(f, v_name, v_id, k, i):
    f.write(longstr.format(name1 = i + 48, sid = v_id, text1 = str(v_id) + "_label", name2 = i, videonumber = v_name, text2 = str(v_id)))
    f.write("    </SlideshowTreeNode>\n")

with open('Kex.oga', 'w') as f:
    f.write(prestr)
    for grpnum, videos in enumerate(l):
        f.write(shortstr.format(num = str(grpnum), grpnum = str(grpnum)))
        for i, (v_name, v_id) in enumerate(videos):
            badognasty(f, v_name, v_id, (grpnum - 1) * + 5 + i)
        f.write("    </SlideshowTreeNode>\n")
    f.write(poststr)

