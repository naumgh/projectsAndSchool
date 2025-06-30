import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShipPlacementComponent } from './ship-placement.component';

describe('ShipPlacementComponent', () => {
  let component: ShipPlacementComponent;
  let fixture: ComponentFixture<ShipPlacementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ShipPlacementComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShipPlacementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
