class Road {
  constructor(x, width, lanes=3) {
    this.x = x
    this.width = width
    this.lanes = lanes
    
    this.left = x - width / 2
    this.right = x + width / 2

    const infinity = 10000000
    this.top =- infinity
    this.bottom = infinity

    const topLeft = {x: this.left, y: this.top}
    const topRight = {x: this.right, y: this.top}
    const bottomLeft = {x: this.left, y: this.bottom}
    const bottomRight = {x: this.right, y: this.bottom}
    this.borders = [
      [topLeft, bottomLeft],
      [topRight, bottomRight]
    ]
  }

  getLaneCenter(laneIndex) {
    const laneWidth = this.width / this.lanes
    return this.left + laneWidth / 2 + laneIndex * laneWidth
  }

  draw(ctx) {
    ctx.lineWidth = 5
    ctx.strokeStyle = "white"
  
    for (let lane=1; lane<=this.lanes-1; lane++) {
      const x = lerp(
        this.left,
        this.right,
        lane / this.lanes
      )
      
      ctx.setLineDash([20, 20])

      ctx.beginPath()
      ctx.moveTo(x, this.top)
      ctx.lineTo(x, this.bottom)
      ctx.stroke()
    }

    ctx.setLineDash([])
    this.borders.forEach(border => {
      ctx.beginPath()
      ctx.moveTo(border[0].x, border[0].y)
      ctx.lineTo(border[1].x, border[1].y)
      ctx.stroke()
    })
  }
}


