import QtQuick

// Animated pixel-art sprite component for Pikagotchi:
// Renders true-color RGBA pet sprites directly with nearest-neighbor crispness
// (smooth: false, mipmap: false). Validates anim against supportedAnims to eliminate
// missing-image 404 warnings in the system journal.
Item {
  id: root

  property string form: "egg"
  property string anim: "idle"
  property string fallbackAnim: "idle"
  property int frameMs: 500
  property bool playing: true
  property color tint: "white" // Kept for API compatibility, unused for full-color RGBA
  property bool mirrored: false

  property int frame: 0

  // Whitelist of valid sprite animations to prevent 404 image load errors in journal
  readonly property var supportedAnims: ["idle", "walk", "climb", "eat", "sleep"]

  readonly property string safeForm: {
    if (root.form === "baby" || root.form === "child" ||
        root.form === "teen_neat" || root.form === "teen_scruffy" ||
        root.form === "adult_ok" || root.form === "adult_gremlin" ||
        root.form === "adult_ace") {
      return root.form
    }
    return "egg"
  }

  readonly property string resolvedAnim: {
    if (root.safeForm === "egg") return "idle"
    if (root.safeForm === "baby" && (root.anim === "walk" || root.anim === "climb")) return "idle"
    if (root.supportedAnims.indexOf(root.anim) !== -1) return root.anim
    if (root.safeForm === "baby" && (root.fallbackAnim === "walk" || root.fallbackAnim === "climb")) return "idle"
    if (root.supportedAnims.indexOf(root.fallbackAnim) !== -1) return root.fallbackAnim
    return "idle"
  }

  function restart() {
    frame = 0
  }

  onAnimChanged: root.restart()
  onFormChanged: root.restart()

  Image {
    id: image
    anchors.fill: parent
    source: Qt.resolvedUrl("assets/sprites/" + root.safeForm + "_" + root.resolvedAnim
      + "_" + (root.frame === 0 ? "a" : "b") + ".png")
    smooth: false
    mipmap: false
    fillMode: Image.PreserveAspectFit
    mirror: root.mirrored
    visible: true
  }

  Timer {
    interval: root.frameMs
    running: root.playing && root.visible
    repeat: true
    onTriggered: root.frame = root.frame === 0 ? 1 : 0
  }
}
